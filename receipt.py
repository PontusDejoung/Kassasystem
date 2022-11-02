from datetime import datetime
from product import Product
class ReceiptRow:
    def __init__(self,productName:str, count:int, perPrice:float,campaignDate:str,campaignprice:float,productType:str):
        self.__ProductName = productName
        self.__Count = count
        self.__PerPrice = perPrice
        self.__CampaignDate = campaignDate
        self.__CamapignPrice = campaignprice
        self.__ProductType = productType
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
    def GetProductType(self):
        return self.__ProductType
    def GetCampaignDate(self):
        return self.__CampaignDate
    def GetCampaignPrice(self):
        return self.__CamapignPrice
    def GetTotalCampaign(self):
        return self.__Count * self.__CamapignPrice
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
    def ADD(self,productName:str, count:int, perPrice:float,campaignDate:str,campaignPrice:float,productType:str):
        receiptRow = ReceiptRow(productName,count,perPrice,campaignDate,campaignPrice,productType)
        for prduct in self.__ReceiptRows:
            if prduct.GetName() == receiptRow.GetName():
                prduct.AddCount(count)
                return
        getDate = campaignDate
        if getDate != " ":
            parts = getDate.split(",")
            start = datetime.strptime(parts[0],"%Y-%m-%d").date()
            end = datetime.strptime(parts[1],"%Y-%m-%d").date()
            currentDate = datetime.now().date()
            if start <= currentDate <= end:
                receiptRow = ReceiptRow(productName,count,campaignPrice,campaignDate,perPrice,productType)
                self.__ReceiptRows.append(receiptRow)
                return
        self.__ReceiptRows.append(receiptRow)
        return
    def GetReceiptRows(self):
            return self.__ReceiptRows
    def CheckIfCampaignIsInRange(self,getDate1,getdate2):
        start = datetime.strptime(getDate1,"%Y-%m-%d").date()
        end = datetime.strptime(getdate2,"%Y-%m-%d").date()
        currentDate = datetime.now().date()
        if start <= currentDate <= end:
            return True
        return False 