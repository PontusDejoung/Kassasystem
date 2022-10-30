from product import Product
from receipt import Receipt, ReceiptRow
from datetime import datetime

allGoods = []
with open("products.txt") as file:
    for line in file:
        parts = line.split(";")
        product = Product(parts[0],parts[1],float(parts[2]),parts[3],parts[4],parts[5])
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

def AdminMenu():
    print(f"1. Sök kvitton\n2. Ändra Namn på produkt\n3. Ändra Pris på produkt\n4. Skapa kampanj\n5. Logga ut från Admin meny")
    selectionInAdminMenu = Felhantering((":"),minValue=1,maxValue=4)
    return selectionInAdminMenu
def AdminMenuSelection():
    while True:
        selectionAdminMenu = AdminMenu()
        if selectionAdminMenu == 1:
            receiptSearch()
        elif selectionAdminMenu == 2:
            ChangeNameOnProducts(allGoods)
        elif selectionAdminMenu == 3:
            ChangePriceOnProducts()
        elif selectionAdminMenu == 4:
            createCampaign(allGoods)
        elif selectionAdminMenu == 5:
            return
def createCampaign(allGoods):
    while True:
        for x in allGoods:
            print(x.GetProductId(), x.GetProductName(), x.GetPrice())
        product = input("Skriv in produkt id på produkt du vill skapa kamapanj på")
        findThisProduct = findProducts(product)
        if findThisProduct == None:
            print("Produkten finns inte förösk igen")
            continue
        newPrice = float(input("Sätt nytt pris"))
        campaignDates = CreateCamapignDates()
        with open("products.txt", "r") as produktfil:
            fileCampaignPrice = produktfil.read()
            fileCampaignPrice = fileCampaignPrice.replace(findThisProduct[3], str(newPrice))
        with open("products.txt", "w") as produktfil:
            produktfil.write(fileCampaignPrice)
        with open("products.txt", "r") as produktfil:
            fileCampaignDate = produktfil.read()
            fileCampaignDate = fileCampaignDate.replace(str(findThisProduct[2]), f"{campaignDates[0]},{campaignDates[1]}")
        with open("products.txt", "w") as produktfil:
             produktfil.write(fileCampaignDate)
        for produkt in allGoods:
            if produkt.GetProductId() == product:
                produkt.SetCampaignPrice(str(newPrice))
                produkt.SetCampaignDate(str(campaignDates))
                print("Kampanj är satt")
                return
def CreateCamapignDates():
    while True:
        campaignStartDate = input("Skriv in startdatum på kampanjen i formatet YYYY-MM-DD:")
        campaignEndDate = input("Skriv in slutdatum på kampanjen i formatet YYYY-MM-DD:")
        if CheckIfDate(campaignStartDate) == True and CheckIfDate(campaignEndDate) == True:
            return campaignStartDate, campaignEndDate
        else:
            print("Skriv i datumformate YYYY-MM-DD")
            continue
def CheckIfDate(dateStr):
    #dateStr = dateStr
    format = "%Y-%m-%d"
    try:
        datetime.strptime(dateStr, format)
        return True
    except ValueError:
        return False


def receiptSearch():
    while True:
        try:
            inputDate = input("Skriv in datum i format YYYY-MM-DD som du vill söka efter")
            time = datetime.strptime(inputDate, "%Y-%m-%d")
        except ValueError:
            print("Fel datum format, formatet ska vara (yyyymmdd)")
            continue
        with open("receipts.txt","r") as file:
            for lines in file:
                if lines.startswith("Kvitto:"):
                    parts = lines.split(" ")
                    splitparts = str(parts[2])
                    split = datetime.strptime(splitparts,"%Y-%m-%d-%H:%M:%S").date()
                    start = split
                    currentdate = time.date()
                    if start != currentdate:
                        print("Hittade inget kvitto på det datumet")
                        return
                    print(lines)
                    if lines.startswith("Total:"):
                        print(lines)
        fullreceipt = input("Vill du se fullständigt kvitto från alla den dagen? Ja/Nej: ").lower()
        if fullreceipt[0] == "j":
            with open("receipts.txt","r") as file:
                for lines in file:
                    print(lines)
        input("Tryck valfri tangent för att återgå till Admin menyn")
        return
def ChangePriceOnProducts():
    pass
def ChangeNameOnProducts(allGoods):
    while True:
        for x in allGoods:
            print(x.GetProductName())
        choice = input("Ange namn på produkt du vill ändra namn på: ").capitalize()
        findProducts = findProductsWithName(choice)
        if findProducts == False:
            print("Produkten finns inte")
            continue
        elif findProducts == True:
            newName = input("Ange nytt namn: ").capitalize()
        with open("products.txt", "r") as produktfil:
            filedata = produktfil.read()
            filedata = filedata.replace(choice, newName)
        with open("products.txt", "w") as produktfil:
            produktfil.write(filedata)
        for produkt in allGoods:
            if produkt.GetProductName() == choice:
                produkt.SetNewName(newName)
                print("Nytt namn är satt")
                return
def findProductsWithName(productname:str):
    for x in allGoods:
        if x.GetProductName() == productname:
            return True
    return False

def findProducts(productid):
    for x in allGoods:
        if x.GetProductId() == productid:
            return x.GetProductName(),x.GetPrice(),x.GetCampaignDate(),x.GetCampaignPrice()
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
        file.write(f"Kvitto: {receiptNumber} {receipt.GetDate()}")
        for row in findReceiptRow:
            file.write(f" \n{row.GetName()} {row.GetCount()} * {row.GetPerPrice()} = {row.GetTotal()}")
        file.write(f"\nTotal:{receipt.GetTotalSum()}\n\n")
def FindReceiptNumber():
    with open("receiptnumber.txt", "r") as file:
        number = file.readline()
        newNumber = int(number) + 1
        with open("receiptnumber.txt", "w") as file:
            file.write(str(newNumber))
    return number
def PrintReceipt(receipt,findReceiptRow):
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
                campaignDate = findProduct[2]
                campaignPrice = findProduct[3]
                receipt.ADD(namn,int(antal),float(belopp),campaignDate,float(campaignPrice))
                findReceiptRow = receipt.GetReceiptRows()
                PrintReceipt(receipt,findReceiptRow)
while True:
    selection = PrintMenu()
    if selection == 0:
        AdminMenuSelection()
    elif selection == 1:
        NewReceipt()
    elif selection == 2:
        break