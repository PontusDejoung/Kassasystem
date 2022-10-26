from ast import Add
from datetime import datetime
from typing import Counter
from product import Product


class ReceiptRow:
    def __init__(self,productName, count, perPrice):
        self.__ProductName = productName
        self.__Count = count
        self.__PerPrice = perPrice
    def AddCount(self,count):
        self.__Count = self.__Count + count
    def GetTotal(self):
        return self.__Count * self.__PerPrice
    def GetName(self):
        return self.__ProductName
    def GetCount(self):
        return self.__Count
    def GetPerPrice(self):
        return self.__PerPrice
# jag borde skapa GetReceiptRowTotal(self) get total
class Receipt:
    def __init__(self):
        self.__Datum = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        self.__ReceiptRows = []
    def GetTotalSum(self):
        sum = 0
        for row in self.__ReceiptRows:
            sum = sum + row.GetTotal()
            return sum
    def GetDate(self):
        return self.__Datum
    def ADD(self,productName:str, count:int, perPrice:float):
        #Finns redan en receiptrow me ddenna productName
        # loopa igenom self.__ReceiptRows och försöka hitta
        # rec.AddcCount
        #ja -> uspdatera count
        #receiptRow = ReceiptRow(productName,count,perPrice)
        receiptRow = ReceiptRow(productName,count,perPrice)
        for prduct in self.__ReceiptRows:
            if prduct.GetName() == receiptRow.GetName():
                prduct.AddCount(count)
                return 
        self.__ReceiptRows.append(receiptRow)
    def GetReceiptRows(self,productname):
        # for productname in self.__ReceiptRows:
        #     return productname
        for product in self.__ReceiptRows:
            if product.GetName() == productname:
                return product#product.GetName(),product.GetCount(),product.GetPerPrice()
