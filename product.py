class Product:
    def __init__(self,productId:str,productName:str, price:float, productType:str):
        self.__ProductName = productName
        self.__Price = price
        self.__ProductId = productId
        self.__ProductType = productType
    def GetProductName(self):
        return self.__ProductName
    def GetProductId(self):
        return self.__ProductId
    def GetPrice(self):
        return self.__Price