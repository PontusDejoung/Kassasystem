from product import Product
from receipt import Receipt, ReceiptRow
from datetime import datetime



allGoods = []
with open("products.txt") as file:
    for line in file:
        parts = line.split(";")
        product = Product(parts[0],parts[1],float(parts[2]),parts[3])
        allGoods.append(product)

def Felhantering(prompt,minValue:int, maxValue:int)->int:
    while True:
        try:
            selection = int(input(prompt))
            if selection < minValue or selection > maxValue:
                 print(f"Mata in ett tal mellan {minValue} och {maxValue} tack")
            else:
                 break
        except ValueError:
             print("Mata in ett tal tack")
             continue
    return selection

def Admin():
    pass
def findProducts(productid):
    for x in allGoods:
        if x.GetProductId() == productid:
            return x.GetProductName(),x.GetPrice()
    return None
def splitParts():
    while True:
        cashierAction = input("Kommando:")
        parts = cashierAction.split(' ')
        if len(parts) == 2:
            return parts[0],parts[1]
        elif parts[0] == "pay":
            return parts
def SaveReceiptToFile(findReceiptRow,receipt):
    receiptNumber = FindReceiptNumber()
    with open("receipts.txt","a") as file:
        file.write(f"Kvitto {receiptNumber} {receipt.GetDate()}\n")
        for row in findReceiptRow:
            file.write(f"{row.GetName()} {row.GetCount()} * {row.GetPerPrice()} = {row.GetTotal()}\n")
        file.write(f"Total:{receipt.GetTotalSum()}\n\n")
def FindReceiptNumber():
    with open("receiptnumber.txt", "r") as file:
        number = file.readline()
        newNumber = int(number) + 1
        with open("receiptnumber.txt", "w") as file:
            file.write(str(newNumber))
    return number
def PrintShopingCart(receipt,findReceiptRow):
        print(f"Kvitto {receipt.GetDate()}")
        for row in findReceiptRow:
            print(f"{row.GetName()} {row.GetCount()} * {row.GetPerPrice()} = {row.GetTotal()}")
        print(f"Total:{receipt.GetTotalSum()}")
def PrintMenu()->int:
    print("0. Admin")
    print("1. Ny kund")
    print("2. Avsluta")
    selectionInMenu = Felhantering((":"),minValue=0,maxValue=2)
    return selectionInMenu
def NewReceipt():
    while True:
        receipt = Receipt()
        while True:
            namn = ""
            belopp = 0
            print("Kassa")
            print("Kommandon:")
            print("<productid> <antal>")
            print("PAY")
            parts = splitParts()
            if parts[0] == "pay":
                SaveReceiptToFile(findReceiptRow,receipt)
                return
            else:
                productid = parts[0]
                antal = parts[1]
                findProduct = findProducts(productid)
                if findProduct == None:
                    print("Produkten finns inte, försök igen")
                    continue
                namn = findProduct[0]
                belopp = findProduct[1]
                receipt.ADD(namn,int(antal),float(belopp))
                findReceiptRow = receipt.GetReceiptRows()
                PrintShopingCart(receipt,findReceiptRow)
while True:
    selection = PrintMenu()
    if selection == 0:
        Admin()
    elif selection == 1:
        NewReceipt()
    elif selection == 2:
        break