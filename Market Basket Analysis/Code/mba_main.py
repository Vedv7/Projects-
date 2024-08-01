import heapq
import pandas as pd

def RecommendItems(CurItemOfInterest, CustomerID, Country, Time, Date):
    data = pd.read_csv('G2/cleaned_data.csv', low_memory=False)

    invo_no = data[(data['StockCode'] == CurItemOfInterest) &
                   (data['Country'] == Country) &
                   (data['date'] == Date)]['InvoiceNo'].tolist()

    item_cnt = {}

    for invo in invo_no:
        d = data[data['InvoiceNo'] == invo]['StockCode']
        for item in d:
            if item in item_cnt:
                item_cnt[item] += 1
            else:
                item_cnt[item] = 1

    maxHeap = []
    for key, value in item_cnt.items():
        maxHeap.append((-value, key))

    heapq.heapify(maxHeap)

    ans = []
    r = min(10, len(maxHeap))
    for i in range(r):
        value, key = heapq.heappop(maxHeap)
        ans.append(key)

    del data

    return ans


# a = RecommendItems("85123A", 'pass', 'United Kingdom', 'pass', '12/1/2010')
# print(a)