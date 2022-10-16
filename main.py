from product import Product


allGoods = []
with open("products.txt") as file:
    for line in file:
        parts = line.split(";")
        product = Product(parts[1],float(parts[2]),parts[0])
def PrintMenu()->int:
    print("0. Admin")
    print("1. Ny kund")
    print("2. Avsluta")
    selectionInMenu = Felhantering((":"),minValue=0,maxValue=2)
    return selectionInMenu
def NewReceipt(allGoods):
    while True:
        print("Kassa")
        datum = 2022-10-16
        print(f"KVITTO: {datum}")
        print("Kommandon:")
        print("<productid> <antal>")
        print("PAY>")
        action = input("Kommandon:")
        if action == "PAY":
            break
        receipt = Receipt()
        receipt.Add("")
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
        NewReceipt(allGoods)
    elif selection == 2:
        break