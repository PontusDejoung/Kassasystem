
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
        file.write(f"{receipt.GetDate()}\n{findReceiptRow.GetName()} {findReceiptRow.GetCount()} * {findReceiptRow.GetPerPrice()} = {total}\n")

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
        shoppinglist = []
        while True:
            print("Kassa")
            #print(f"Kvitto {receipt.GetDate()}")
            print("Kommandon:")
            print("<productid> <antal>")
            print("PAY")
            parts = splitParts()
            if parts[0] == "pay":
                SaveReceiptToFile(findReceiptRow,total,receipt)
                return
            else:
                productid = parts[0]
                antal = parts[1]
                findProduct = findProducts(productid)
                if findProduct == None:
                    print("Produkten finns inte, försök igen")
                namn = findProduct[1]
                belopp = findProduct[2]
                receipt.ADD(namn,int(antal),float(belopp))
                findReceiptRow = receipt.GetReceiptRows(namn)
                total = receipt.GetTotalSum()
                saveRow = shoppinglist.append(f"")
            #PrintShopingCart(receipt,findReceiptRow,total)
            print(f"Kvitto {receipt.GetDate()}\n{findReceiptRow.GetName()} {findReceiptRow.GetCount()} * {findReceiptRow.GetPerPrice()} = {total}\nTotal:{total}")
            #print(f"Kvitto {receipt.GetDate()}\n{findReceiptRow[0]} {findReceiptRow[1]} * {findReceiptRow[2]} = {total}\nTotal:{total}")
def PrintShopingCart(receipt,findReceiptRow:list,total):
        print(f"\nKVITTO: {receipt.GetDate()}")
        for rad in findReceiptRow:
            print(f"{rad.GetName()}")
        print(f"Total:{total}")
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