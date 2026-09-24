import math
binaryList = []
hexaList = []

def calculateLoop(quotient, remainder):
    while quotientChecker == True:
        concatenation(hexaList, int(quotient), int(remainder))
        quotient = quotient / 16
        remainder = quotient * 16
        print("The quotient and remainder are :", quotient, remainder)
        if quotient <= 0:
            quotientChecker == False
            concatenation(hexaList, int(quotient), int(remainder))
    else:
        concatenation(hexaList, " ", " ")



def concatenation(hexaList, quotient, remainder):
  while quotient != " ":
    quotientPlaceholder = str(quotient)
    remainderPlaceholder = str(remainder)
    hexaList =  quotientPlaceholder +"R"+ remainderPlaceholder
    return hexaList
  else:
    hexaList = " "
    return hexaList

def hexadecimaList(hexaList):
    index = int(0)
    hexaList.reverse()
    while index <= hexaList:
        print(hexaList)





# ----------------- MAIN FUNCTION ------------------
quotient = float()
remainder = int()
quotientChecker = True

numSelect = int(input("\nEnter a whole number to find the hexadecimal: "))
quotient = numSelect / 16
print(quotient)
remainder = numSelect % 16
print(remainder)
calculateLoop(int(quotient), remainder)
#hexadecimaList(hexaList)