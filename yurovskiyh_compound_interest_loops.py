#Timothy
#Compound Interest
# FV = PV(1+r/m)**mt
#What did you like?
#I liked coding the while loop
#What did you struggle with?
#I definitely struggled with getting the for loop to work correctly
#The common difference between while and for loops:
#While loops have no end unless specified.
#For loops have a start, a stop, and often times a step as well.
#I used a for loop for the monthly compounding because there is a goal amount that is set by the user.
#I used the while loop for the data validation and the month amount it would take to reach the goal
#because these variables are not definite and change based upon user input.
#6 loops total
#Top 3 things I learned: error handling with while loops,
#make sure to use +1 on for loops where it's necessary,
#use 'break' to escape loops

#User input. Using try and except for error handling and if statements for data validation.
#the 'continue' keeps the loop from exiting until a correct value is entered
while True:
    try:
        fDepositTY = float(input("Enter starting deposit amount: "))
        if fDepositTY <= 0:
            print("Input must be >0")
            continue
        break
    except ValueError:
        print("Use the correct data types. Numbers >0")
while True:
    try:#The annual rate is converted to a decimal
        fAnnualRateTY = float(input("Enter the interest rate percentage: "))/100
        if fAnnualRateTY <= 0:
            print("Input must be >0")
            continue
        break
    except ValueError:
        print("Use the correct data types. Numbers >0")
while True:
    try:
        iMonthsTY = int(input("Enter the number of months: "))
        if iMonthsTY <= 0:
            print("Input must be whole numbers >0")
            continue
        break
    except ValueError:
        print("Use the correct data types. Whole numbers >0")
while True:
    try:
        fGoalTY = float(input("What is the goal amount? Must be >=0 "))
        if fGoalTY < 0:
            print("Input must be >0")
            continue
        break
    except ValueError:
        print("Use the correct data types. Numbers >0")

#Mathematical operations
#Divide the annual rate to get the monthly rate
fMonthlyRateTY = fAnnualRateTY / 12
#initialize account balance =  deposit amount
fBalanceTY = fDepositTY
#For loop which cycles through every month
#and compounds the interest for each month
for iMonthsLTY in range(1, iMonthsTY + 1):
    #Calculate the interest rate by multiplying the balance by the monthly rate
    fInterestRateTY = fBalanceTY * fMonthlyRateTY
    #Add the calculated interest rate to the balance for every month.
    fBalanceTY += fInterestRateTY
    #Print the number of months along with the account balance, formatted
    print(f"Month: {iMonthsLTY}. Account balance is: ${fBalanceTY:,.2f}")

#Initialize monthly goal variable
iMonthGoalTY = 0
#Savings account = starting deposit
fSavingsTY = fDepositTY
#while savings amount is less than goal amount
while fSavingsTY < fGoalTY:
    #calculate the interest rate, add it to savings account
    fSavingsInterestRateTY = fSavingsTY * fMonthlyRateTY
    fSavingsTY += fSavingsInterestRateTY
    iMonthGoalTY += 1
    #Print out calculations formatted
if fGoalTY > 0:
    print(f"It will take: {iMonthGoalTY} month(s) to reach the goal of ${fGoalTY:,.2f}")
    exit()
else:
    print("Thank you. Come again!")
    exit()