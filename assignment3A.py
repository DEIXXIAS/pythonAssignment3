# initializing my list that I will use to append any remainder to
hexaList =[]

def calculations(userInput): # where I will calculate the userInput 
    if userInput == 0: # if the users input reaches zero, meaning that the quotient is 0
        return "" # it will return empty
    else: # otherwise we will run both the calculations for the quotient and then append it to the hexalist
        calculations(userInput // 16) 
        hexaCalculations(userInput % 16, hexaList) 



def hexaCalculations(remainder, hexaList): # when the quotient is not zero and we have a remainder
    if remainder <= 9: # if the remainder falls between 0-9
       hexaList.append(str(remainder)) # we will append it to the hexa list as a str
    elif remainder == 10: # if it is greater than 10-15, it will be given a letter between A-F
        hexaList.append("A")
    elif remainder == 11:
        hexaList.append("B")
    elif remainder == 12:
        hexaList.append("C")
    elif remainder == 13:
        hexaList.append("D")
    elif remainder == 14:
        hexaList.append("E")
    elif remainder == 15:
        hexaList.append("F")
    else: #if it happens to not fall outside this range, append it as a str
        hexaList.append(str(remainder))


# ----------------- MAIN FUNCTION ------------------
# asking the user what number they want to find as the hexadecimal 
userInput = int(input("Enter a whole number to find the hexadecimal value: "))
if userInput == 0: # if the user inputs a number equal to zero
    print("0") #return zero
else: # otherwise run the calculations and then print the joined hexalist once it is finished with calculations
    calculations(userInput)
    print("".join(hexaList))