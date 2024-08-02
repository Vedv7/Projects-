
# -*- coding: utf-8 -*-
"""


Original file is located at
    Neural Network: https://colab.research.google.com/drive/19gtmUwfXaBXj7-x81ov10sw4MVqUUR1K?usp=sharing
    OLS: https://colab.research.google.com/drive/1QmTQzCT7Q5F6PY1l77UK-KQ-mgrmvlYn?usp=sharing
Important Note:
- Please install the required packages, they are [keras, numpy, pandas, matplotlib]
- The output is a graph, where the recommended price is given at the top right of the graph

"""

# Importing
import warnings
warnings.filterwarnings("ignore")
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import keras
from joblib import load

def RecommendPrice(itemId, data=None, time=None, date=None):

    # Load the normalized data
    data_n = pd.read_csv('GX/artifacts/normalized_data.csv')
    data = pd.read_csv('GX/artifacts/data.csv')

    # Load the model from the specified path
    model_path = 'GX/artifacts/model_nn2.h5'
    loaded_model = keras.models.load_model(model_path)

    # Load the normalizer
    scaler_path = 'GX/artifacts/scaler.joblib'
    loaded_scaler = load(scaler_path)

    # Getting the price points for the model
    # input = data[data['sku_id'] == normItemId].iloc[0].drop('price').tolist()
    prices = data[data['sku_id'] == itemId]['price'].unique().tolist()
    prices.sort()
    sales = data[data['sku_id'] == itemId]['sales'].unique().tolist()
    maxPrice, minPrice = max(prices), min(prices)
    maxSales, minSales = max(sales), min(sales)
    cost = data[data['sku_id'] == itemId]['cost'].iloc[0] / 100

    # predictions
    predProfit = {}
    for price in prices:
        normItemId = round((itemId - 0) / (399 - 0), 5)
        normPrice = round((price - minPrice) / (maxPrice - minPrice), 5)
        input = data_n[(data_n['sku_id'] == normItemId) &
                       (data_n['price'] == normPrice)].iloc[0].drop('sales').tolist()
        input = numpy.array(input)
        predictions = loaded_model.predict(numpy.reshape(input, (1, 18)))
        predSales = predictions * (maxSales - minSales) + minSales
        profit = predSales * (price - cost)
        predProfit[profit[0][0]] = price

    # plotting
    plt.figure(figsize=(10, 5))
    plt.plot(predProfit.values(), predProfit.keys())
    plt.scatter(predProfit[max(predProfit)], max(predProfit), color='red')
    text = "Best price: " + str(predProfit[max(predProfit)]) + "\n" + "Profit: " + str(max(predProfit))
    plt.text(prices[-1] - .3, max(predProfit) - 20, text, fontsize=12, color='black', ha='left')
    plt.xlabel('Price')
    plt.ylabel('Profit')
    plt.title('Price vs Profit curve for ItemID: ' + str(itemId))
    plt.show()

    return predProfit[max(predProfit)]
