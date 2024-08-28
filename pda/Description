Project: Heart Disease Prediction Using Logistic Regression

1.	Introduction

This project focuses on predicting the risk of heart disease over ten years using the Framingham Heart Study dataset. The analysis involves data preparation, exploratory data analysis, logistic regression modeling, and model evaluation.

2.	Data Preparation

•	Loading the Data: The dataset is loaded using read.csv().
•	Feature Renaming: Columns are renamed for clarity and readability:
o	male to Sex_male
o	currentSmoker to IsCurrentSmoker
o	cigsPerDay to CigarettesPerDay
o	... (continue with the rest of the renaming)
•	Handling Missing Values: Missing values are identified and removed using na.omit().

3.	Exploratory Data Analysis (EDA)

•	Visualizing Distributions: Histograms for all features are created using a custom draw_histograms() function.
•	Count Plot for Target Variable: A bar plot is generated to show the distribution of the target variable TenYearCHDRisk.
•	Summary Statistics: Descriptive statistics are computed for the dataset using the summary() function.

4.	Logistic Regression Modeling

•	Building the Initial Model: A logistic regression model is fitted using all available features.
•	Backward Elimination: The step() function is used for backward elimination to refine the model by removing non-significant features.
•	Model Summary: The final model is summarized, showing the significance of each predictor.

5.	Model Evaluation

•	Odds Ratios and Confidence Intervals: Extracted and printed using exp() for easier interpretation.
•	Data Splitting: The dataset is split into training and testing sets with an 80/20 ratio using sample.split().
•	Model Training: Logistic regression is performed on the training data.
•	Prediction: Probabilities are predicted for the test set, and a threshold of 0.5 is applied to classify outcomes.

6.	Confusion Matrix and Metrics

•	Confusion Matrix: Created using confusionMatrix() to evaluate model performance.
•	Calculation of Metrics:
o	Accuracy: Proportion of correct predictions.
o	Sensitivity: True positive rate.
o	Specificity: True negative rate.
o	Positive Predictive Value (PPV) and Negative Predictive Value (NPV): Calculated manually.
o	Positive Likelihood Ratio (PLR) and Negative Likelihood Ratio (NLR): Also calculated manually.
•	Metrics Reporting: All the above metrics are printed for model evaluation.

7.	ROC Curve and AUC

•	ROC Curve: Generated using roc() to visualize model performance across different thresholds.
•	AUC (Area Under the Curve): Calculated to assess the overall model accuracy.

8.	Conclusion

•	Significance of Features: Attributes retained after backward elimination have p-values below 5%, indicating significance in predicting heart disease.
•	Risk Factors: Features like age, smoking, and systolic blood pressure are highlighted as increasing the odds of heart disease.
•	Model Performance: The model achieved an accuracy of x% (replace with actual value) and an AUC of y (replace with actual value), suggesting it is satisfactory but could be improved with more data.
