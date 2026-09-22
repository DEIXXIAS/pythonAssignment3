binaryList = []

def convertBinary(binaryList, numSelect):
    product = numSelect / 2

    while numSelect != 0:
        if product.isdecimal():
            numSelect = numSelect - 1 
            binaryList.insert(1, '1')
            product = numSelect / 2
            return

        else:
            binaryList.insert(1, '0')
            numSelect = product
            return



def hexadecimalConversion(binaryList):
    index = int(0)

    







# ----------------- MAIN FUNCTION ------------------

numSelect = int(0)

numSelect = input("\nEnter a whole number to find the hexadecimal: ")
convertBinary(binaryList, numSelect)
hexadecimalConversion(binaryList)
