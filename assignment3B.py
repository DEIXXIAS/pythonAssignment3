
remainderList = []

def GCD(largerUserInput, smallerUserInput):
    remainder = int()
    remainder = largerUserInput % smallerUserInput
    print(remainder)
    remainderList.append(remainder)
    index = 0
    while remainder != 0:
        largerUserInput = smallerUserInput
        smallerUserInput = remainder
        remainder = largerUserInput % smallerUserInput
        remainderList.append(remainder)
        index += 1
    else:
        print("\nThe GCD is:", remainderList[index-1])



#=-----------------------------------------------MAIN PROGRAM---------------------------------------------------------=#

print("\nWelcome to Vincent's Greatest Common Divisor Program")
largerUserInput = int(input("\nEnter in the larger value you want to find the GCD for: "))
smallerUserInput = int(input("\nEnter the second smaller value you want to find the GCD for: "))
GCD(largerUserInput, smallerUserInput)

