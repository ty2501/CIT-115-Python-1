'''Timothy
Capstone Project - Banking System
Prof. C
What I liked about the assignment?
Formatting the output to appear as shown in the examples
What I struggled with?
The transactionHistory function was most challenging
I've learned how to think from a different perspective
Each project up to this point has been challenging, but fun.
This one takes the cake. The first assignment,
which was the interplanetary weights, was mainly on constants, user input, and formatting.
The final project utilized a lot of user input and formatting.
The second assignment was the compound interest program,
which took user input and calculated how much money would compound over a user inputted amount of years.
The third project utilized if else statements to convert temperatures from F to C, and vice versa.
This program also had error handling for temperatures that would exceed the boiling point.
This error handling carried onward and advanced into a more robust and complete version;
included in this final project, as well as previous projects, as a function.
Ultimately each project was more elaborate than the one before it, and included more programming logic.
I enjoyed working with lists and tuples on this project. Looking forward to Py2.
'''

print("Welcome to Tim's Banking System")
def PromptForInput(prompt): #data validation function
    while True:
        try:
            inputTY = float(input(prompt))
            if inputTY > 0:
                return inputTY
            else:
                print("Enter a number >0")
        except ValueError:
            print("Enter a numeric value")

def userDeposit(accountBalanceTY, transactions): #user deposit function, takes in account balance and transactions list
    depositAmount = PromptForInput("Enter a deposit amount: ") #deposit input
    accountBalanceTY += depositAmount #add deposited amount to account balance
    transactions.append((depositAmount, "deposited")) #add the amount to the transactions list, and save it under a tuple label as a deposit
    print(f"Deposit Successful. Account balance: ${accountBalanceTY:,.2f}")
    return accountBalanceTY
def userWithdrawal(accountBalanceTY, transactions): #the opposite of the deposit function
    withdrawAmount = PromptForInput("Enter a withdrawal amount: ")
    if withdrawAmount > accountBalanceTY: #handle insufficient funds
        print("Insufficient funds")
    else:
        accountBalanceTY -= withdrawAmount #subtract withdrawal amount from balance
        transactions.append((-withdrawAmount, "withdrawn")) #add it to the list and label it with a tuple. subtract symbol required to prevent the transaction history from showing negatives
        print(f"Withdrawal successful. Account balance: ${accountBalanceTY:,.2f}")
    return accountBalanceTY
def transactionHistory(transactions, accountBalanceTY):
    outputTY = [] #declare list
    outputTY.append("Tim's Banking System\n") #heading
    if not transactions: #check if the transactions list is empty
        outputTY.append(f"{'No transactions processed.':<40}\n") #left align 40 spaces
        outputTY.append(f"Account Balance: ${accountBalanceTY:>8,.2f}\n")
        return "".join(outputTY) #condense list into one string, with empty string seperator
    outputTY.append("Transaction history:\n")
    outputTY.append(f"+{'-'*40}+\n") #upper line
    for i, typeTY in transactions: #loop through list, for each tuple, i receives the amount and typeTY assigns the label
        if typeTY == "deposited":
            labelTY = "Deposited:"
        elif typeTY == 'withdrawn':
            labelTY = "Withdrawn:"
        else:
            labelTY = "Interest:"
        outputTY.append(f"|{labelTY:<30}${abs(i):>8,.2f} |\n") #formats each transaction from the previous loop, right aligned and left aligned, abs() finds absolute value to prevent negatives from showing in transaction history
    outputTY.append(f"+{'-'*40}+\n") #lower line
    outputTY.append(f"|{'Number of transactions:':<30}{len(transactions):>10}|\n") #adds the number of transactions to the list
    outputTY.append(f"|{'Current Balance:':<30}${accountBalanceTY:>8,.2f}|\n") #adds balance to the list
    return "".join(outputTY) #condense the list into a string
def interestApplication(accountBalanceTY, transactions):
    if accountBalanceTY == 0: #handle zero balance
        print("Account Balance: $0, no interest will be applied")
        return accountBalanceTY
    interestRateTY = PromptForInput("Enter a interest rate: ") / 100 #math
    rateTY = interestRateTY / 12
    interestCalculatedTY = accountBalanceTY * rateTY
    interestTotalTY = accountBalanceTY + interestCalculatedTY #calculates the total interest amount
    transactions.append((interestCalculatedTY, "interest")) #add to the transactions list and label it interest
    print(f"Interest applied: ${interestCalculatedTY:,.2f}  New balance: ${interestTotalTY:,.2f}") #prints out applied interest
    return interestTotalTY
def produceStatement(transactions, accountBalanceTY): #function that writes strings to a file
    #declare filename
    filename = "tyBankStatement.txt"
    #open the file and print the results of transaction history function
    with open(filename, "w") as file:
        file.write(transactionHistory(transactions, accountBalanceTY)) #takes in transactions and account balance
def main():
    transactions = [] #declare variables
    accountBalanceTY = 0 #menu screen
    print("1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. View Transaction History\n5. Calculate and Apply Interest\n6. Exit")
    while True: #loop to prompt user for input
        userInput = int(PromptForInput("Enter your choice: "))
        if userInput == 1:
            accountBalanceTY = userDeposit(accountBalanceTY, transactions) #deposit function
        elif userInput == 2:
            accountBalanceTY = userWithdrawal(accountBalanceTY, transactions) #balance function
        elif userInput == 3:
            print(f"Account Balance: ${accountBalanceTY}") #prints account balance
        elif userInput == 4:
            print(transactionHistory(transactions, accountBalanceTY)) #prints transaction history
        elif userInput == 5:
            accountBalanceTY = interestApplication(accountBalanceTY, transactions) #calculate interest
        elif userInput == 6:
            print("Thank you for banking with us! Bye!") #closing statement, write to file in current directory
            produceStatement(transactions, accountBalanceTY)
            break #end loop
        else:
            print("Enter between 1-6") #error handling


main()