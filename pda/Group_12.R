# Load necessary libraries
library(readr)
library(dplyr)
library(ggplot2)
library(stats)
library(caret)
library(pROC)
library(MASS)
library(caTools)  # For sample.split

# Data Preparation
heart_df <- read.csv("C:/Users/vedas/Desktop/pda/framingham.csv")
heart_df$education <- NULL
names(heart_df)[names(heart_df) == 'male'] <- 'Sex_male'
names(heart_df)[names(heart_df) == 'currentSmoker'] <- 'IsCurrentSmoker'
names(heart_df)[names(heart_df) == 'cigsPerDay'] <- 'CigarettesPerDay'
names(heart_df)[names(heart_df) == 'BPMeds'] <- 'OnBPMedication'
names(heart_df)[names(heart_df) == 'prevalentStroke'] <- 'HistoryOfStroke'
names(heart_df)[names(heart_df) == 'prevalentHyp'] <- 'HasHypertension'
names(heart_df)[names(heart_df) == 'diabetes'] <- 'HasDiabetes'
names(heart_df)[names(heart_df) == 'totChol'] <- 'TotalCholesterol'
names(heart_df)[names(heart_df) == 'sysBP'] <- 'SystolicBP'
names(heart_df)[names(heart_df) == 'diaBP'] <- 'DiastolicBP'
names(heart_df)[names(heart_df) == 'BMI'] <- 'BodyMassIndex' 
names(heart_df)[names(heart_df) == 'heartRate'] <- 'HeartRate'
names(heart_df)[names(heart_df) == 'glucose'] <- 'GlucoseLevel'
names(heart_df)[names(heart_df) == 'TenYearCHD'] <- 'TenYearCHDRisk'


# Handling Missing Values
missing_values <- colSums(is.na(heart_df))
print(missing_values)
count <- sum(missing_values > 0)
cat('Total number of rows with missing values is ', count, '\n')
cat('Since it is only', ((count / nrow(heart_df)) * 100), 'percent of the entire dataset, the rows with missing values are excluded.\n')
heart_df <- na.omit(heart_df)


# Exploratory Analysis
draw_histograms <- function(dataframe, features, rows, cols) {
  par(mfrow = c(rows, cols))
  for (feature in features) {
    hist(dataframe[[feature]], main = paste(feature, "Distribution"), xlab = feature, col = 'midnightblue')
  }
}
draw_histograms(heart_df, names(heart_df), 6, 3)

# Count plot for TenYearCHD
table(heart_df$TenYearCHDRisk)
ggplot(heart_df, aes(x = TenYearCHDRisk)) + geom_bar() + labs(title = "Distribution of TenYearCHD")


# Summary statistics
summary(heart_df)

# Logistic Regression
model <- glm(TenYearCHDRisk ~ ., data = heart_df, family = binomial())
summary(model)

# Assuming heart_df is your dataframe and TenYearCHD is the response variable
full_model <- glm(TenYearCHDRisk ~ ., data = heart_df, family = binomial())

# Perform backward elimination
backward_model <- step(full_model, direction = "backward")

# To print the summary of the final model
summary(backward_model)


# To extract and print odds ratios, confidence intervals, and p-values
exp_coef <- exp(coef(backward_model))
conf_int <- exp(confint(backward_model))
p_values <- coef(summary(backward_model))[, "Pr(>|z|)"]
results <- cbind(Odds_Ratio = exp_coef, CI_95_2_5 = conf_int[, 1], CI_95_97_5 = conf_int[, 2], P_Value = p_values)
print(results)

# Data Splitting
set.seed(5)  # Align with Python's random_state
split <- sample.split(heart_df$TenYearCHDRisk, SplitRatio = 0.8)
train_data <- subset(heart_df, split == TRUE)
test_data <- subset(heart_df, split == FALSE)

# Model Training
logreg <- glm(TenYearCHDRisk ~ . - 1, data = train_data, family = binomial()) 

# Prediction
y_pred_prob <- predict(logreg, newdata = test_data, type = "response")
threshold <- 0.5
y_pred <- ifelse(y_pred_prob > threshold, 1, 0)


# Model Evaluation
cm <- confusionMatrix(as.factor(y_pred), as.factor(test_data$TenYearCHDRisk))

# Extracting Specific Metrics
accuracy <- cm$overall['Accuracy']
misclassification <- 1 - accuracy
sensitivity <- cm$byClass['Sensitivity']
specificity <- cm$byClass['Specificity']

# Manually calculate the confusion matrix values
tn <- cm$table[1,1] # True Negatives
fp <- cm$table[1,2] # False Positives
fn <- cm$table[2,1] # False Negatives
tp <- cm$table[2,2] # True Positives

# Manually calculate PPV and NPV with checks for division by zero
ppv <- ifelse((tp + fp) > 0, tp / (tp + fp), NA) # Positive Predictive Value
npv <- ifelse((tn + fn) > 0, tn / (tn + fn), NA) # Negative Predictive Value

# Calculate Likelihood Ratios with checks for division by zero
PLR <- ifelse((1 - specificity) > 0, sensitivity / (1 - specificity), NA)  # Positive Likelihood Ratio
NLR <- ifelse(specificity > 0, (1 - sensitivity) / specificity, NA)  # Negative Likelihood Ratio

# Print Results
cat('Accuracy of the model =', accuracy, '\n')
cat('Misclassification =', misclassification, '\n')
cat('Sensitivity or True Positive Rate =', sensitivity, '\n')
cat('Specificity or True Negative Rate =', specificity, '\n')
cat('Positive Predictive Value =', ppv, '\n')
cat('Negative Predictive Value =', npv, '\n')
cat('Positive Likelihood Ratio =', PLR, '\n')
cat('Negative Likelihood Ratio =', NLR, '\n')


# ROC Curve and AUC
roc_curve <- roc(response = test_data$TenYearCHDRisk, predictor = y_pred_prob)
auc_value <- auc(roc_curve)
plot(roc_curve)
cat('Area Under The Curve (AUC) =', auc_value, '\n')


# Conclusion
cat("Conclusion:\n",
    "All attributes selected after the elimination process show P-values lower than 5%, suggesting significant role in the Heart disease prediction.\n",
    "Men seem to be more susceptible to heart disease than women.\n",
    "Increase in Age, number of cigarettes smoked per day, and systolic Blood Pressure also show increasing odds of having heart disease.\n",
    "Total cholesterol shows no significant change in the odds of CHD. Glucose too causes a very negligible change in odds.\n",
    "The model predicted with ", cm$overall['Accuracy'], " accuracy.\n",
    "The Area under the ROC curve is ", auc_value, ", which is somewhat satisfactory.\n",
    "Overall, the model could be improved with more data.\n")

