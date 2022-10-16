from datetime import datetime


class ReceiptRow:
    def __init__(self):
        self.__ProductName = ""
        self.__Count = 0
        self.__PerPrice = 0
    def GetTotal(self):
        return self.__Count * self.__Price


class Receipt:
    def __init__(self):
        self.__Datum = datetime.now()
        self.__ReceiptRows = []
    def GetTotal(self):
        sum = 0
        for row in self.__ReceiptRows:
            sum = sum + row.GetTotal()
            return sum