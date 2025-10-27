import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):  #changed logs=[] to logs=None
    if logs is None: #added
        logs=[]
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError: #fix--KeyError was added
        pass

def getQty(item):
    return stock_data[item]

def loadData(file="inventory.json"): #changes made
    with open(file, "r") as f:
        global stock_data
        stock_data = json.loads(f.read())

def saveData(file="inventory.json"):  #changes made
    with open(file, "w") as f:
        f.write(json.dumps(stock_data))

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    #eval("print('eval used')")  # dangerous ---this line is removed

main()
