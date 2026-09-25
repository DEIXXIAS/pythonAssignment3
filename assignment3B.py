# assigning a remainder list to store all the remainders that we are using
remainderList = []

#function to figure out the greatest common divisor 
def GCD(largerUserInput, smallerUserInput): # needs to values of the larger value and the smallest value
    remainder = int() # intializing the remainder
    remainder = largerUserInput % smallerUserInput # finding the remainder of the two values
    remainderList.append(remainder) # appending the remainder into the list
    index = 0 # setting our index to zero to find the remainder in our list

    while remainder != 0: # while the value is the remainder is not zero
        largerUserInput = smallerUserInput # setting the lower value into the higher value to find the next remainder
        smallerUserInput = remainder # setting the remainder to the lower value to find the next remainder
        remainder = largerUserInput % smallerUserInput # finding the two remainders of the two values
        remainderList.append(remainder) # appending the new remainder into the list
        index += 1 # increasing the list index
    # once the remainder is 0, we will find the second to last remainder as the last remainder will always store zero
    else: 
        print("\nThe GCD is:", remainderList[index-1]) # printing the GCD



#=-----------------------------------------------MAIN PROGRAM---------------------------------------------------------=#
# printing the main welcome message
print("\nWelcome to Vincent's Greatest Common Divisor Program")
largerUserInput = int(input("\nEnter in the larger value you want to find the GCD for: ")) # asking for user to type a larger value
smallerUserInput = int(input("\nEnter the second smaller value you want to find the GCD for: ")) # asking the user to type a smaller value
GCD(largerUserInput, smallerUserInput) # calling the GCD function to calculate the GCD

