
from argparse import Action
from product import Product
from receipt import Receipt, ReceiptRow
from datetime import datetime



allGoods = []
with open("products.txt") as file:
    for line in file:
        parts = line.split(";")
        product = Product(parts[0],parts[1],float(parts[2]),parts[3])
        allGoods.append(product)


def findProducts(productid):
    for x in allGoods:
        if x.GetProductId() == productid:
            return x,x.GetProductName(),x.GetPrice()
    return None
def splitParts():
    while True:
        cashierAction = input("Kommando:")
        parts = cashierAction.split(' ')
        if len(parts) == 2:
            return parts[0],parts[1]
        elif parts[0] == "pay":
            return parts
def SaveReceiptToFile(findReceiptRow,total,receipt):
    with open("receipts.txt","a") as file:
        file.write(f"{receipt.GetDate()}\n{findReceiptRow[0]} {findReceiptRow[1]} * {findReceiptRow[2]} = {total}\n")

def PrintMenu()->int:
    print("0. Admin")
    print("1. Ny kund")
    print("2. Avsluta")
    selectionInMenu = Felhantering((":"),minValue=0,maxValue=2)
    return selectionInMenu
def NewReceipt():
    while True:
        productid = 0
        antal = 0
        namn = ""
        belopp = 0
        #findReceiptRow = ""
        total = 0
        receipt = Receipt()
        while True:
            print("Kassa")
            print(f"Kvitto {receipt.GetDate()}")
            print("Kommandon:")
            print("<productid> <antal>")
            print("PAY")
            parts = splitParts()
            # productid = str(parts[0])
            # antal = int(parts[1])
            #findProduct = findProducts(splitParts)
            # if findProduct == None:
            #     print("Produkten finns inte, försök igen")
            if parts[0] == "pay":
                SaveReceiptToFile(findReceiptRow,total,receipt)
                return
            else:
                productid = parts[0]
                antal = int(parts[1])
                findProduct = findProducts(productid)
                if findProduct == None:
                    print("Produkten finns inte, försök igen")
                namn = findProduct[1]
                belopp = findProduct[2]
                receipt.ADD(namn,antal,belopp)
                findReceiptRow = receipt.GetReceiptRows(namn)
                total = receipt.GetTotalSum()
                print(f"{findReceiptRow[0]} {findReceiptRow[1]} * {findReceiptRow[2]} = {total}")
          
        # elif len(cashierAction) == 2 and findProducts(cashierAction[0]) == True and cashierAction[1].isnumeric():
        #     returnProducts(cashierAction[0])
        #     # receipt.ADD(product.GetProductName(),int(cashierAction[1]),1.5)
        #     receipt.ADD(str(product.GetProductName()),int(cashierAction[1]),float(product.GetPrice()))
        #     print(f"{product.GetProductName()} {cashierAction[1]} * {product.GetPrice()} = {receipt.GetTotalSum()}")
        #     print(f"Total:{receipt.GetTotalSum()}")
        #     print("Tjoho")
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
while True:
    selection = PrintMenu()
    if selection == 0:
        print("a")
    elif selection == 1:
        NewReceipt()
    elif selection == 2:
        break