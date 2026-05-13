#Timothy
#BDJ Real Estate
#Prof. C
'''What I liked about the assignment? I liked working with the list() function.
What I struggled with? Getting the median to work correctly. Initially I didn't have parentheses so it was only dividing the second value. (computeMedian else: statement)
What is a list? A list is a group of stored data in a variable. Lists can be edited and are stored in order of being entered; unless sorted.
An example of list being useful in previous projects? The grade analyzer.
A list can be used to store all inputted values and then sorted to find the smallest value.
'''
COMMISSION = 0.03

#Data validation function.
def getFloatInput(prompt):
    while True:
        try:
            inputValueTY = float(input(prompt))
            if inputValueTY > 0:
                return inputValueTY
            else:
                print("Value must be >0")
                continue
        except ValueError:
            print("Invalid input - Please enter a numeric value")
#median function.
def getMedian(listTY):
    listTY.sort() #using sort() method
    lengthTY = len(listTY) #this gives us how many items are in the list
    middleTY = lengthTY // 2 #find the middle value
    if lengthTY % 2 != 0: #modulus division to find out if the values are odd or even
        medianTY = listTY[middleTY] #get middle number from list
    else:
        medianTY = (listTY[middleTY - 1] + listTY[middleTY]) / 2 #if there's an even amount, find the average of the 2 middle values
    return medianTY
def main():
    #declare list
    listTY = []
    while True:
        userInput = getFloatInput("Enter property sales value: ")
        listTY.append(userInput) #add value to the list
        enterAnotherTY = ''
        while enterAnotherTY not in ['y','n']:
            enterAnotherTY = input("Enter another value Y or N  ").lower() #input value becomes lowercase
            if enterAnotherTY not in ['y', 'n']:
                print("Enter Y or N") #input validation
        if enterAnotherTY == 'n':
            break #end loop
    computeMedianTY = getMedian(listTY) #call median function,
    totalTY = sum(listTY) #calculate total
    countTY = len(listTY)
    minimumTY = listTY[0] #smallest value
    maximumTY = listTY[-1] #largest value
    averageTY = totalTY / countTY #average the total
    commissionTY = totalTY * COMMISSION #commission
    for indexTY in range(1, len(listTY) + 1): #loop to index the list
        valueTY = listTY[indexTY - 1] #start at 1 instead of 0
        print(f"Property {indexTY:<3} $ {valueTY:14,.2f}") #left align
    print(f"{'Minimum:':12} $ {minimumTY:14,.2f}")#printed results
    print(f"{'Maximum:':12} $ {maximumTY:14,.2f}")
    print(f"{'Total:':12} $ {totalTY:14,.2f}")
    print(f"{'Average:':12} $ {averageTY:14,.2f}")
    print(f"{'Median:':12} $ {computeMedianTY:14,.2f}")
    print(f"{'Commission:':12} $ {commissionTY:14,.2f}")
main()