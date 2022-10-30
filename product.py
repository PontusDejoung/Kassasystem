class Product:
    def __init__(self,productId:str,productName:str, price:float, productType:str,productcampaigndate:str,productcampaignprice:float):
        self.__ProductName = productName
        self.__Price = price
        self.__ProductId = productId
        self.__ProductType = productType
        self.__ProductCampaignDate = productcampaigndate
        self.__ProductCampaignPrice = productcampaignprice
    def GetProductName(self):
        return self.__ProductName
    def GetProductId(self):
        return self.__ProductId
    def GetPrice(self):
        return self.__Price
    def SetNewName(self,newName:str):
        self.__ProductName = newName
    def GetCampaignPrice(self):
        return self.__ProductCampaignPrice
    def GetCampaignDate(self):
        return self.__ProductCampaignDate
    def SetCampaignPrice(self,newPrice:float):
        self.__ProductCampaignPrice = newPrice
    def SetCampaignDate(self, newDate:str):
        self.__ProductCampaignDate = newDate