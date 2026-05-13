#Timothy
#Compound Interest
#What did you like about the assignment
#I enjoyed figuring out and troubleshooting the compounding formula.

#What you struggled with?
#The compounding formula. I had a few variables that were out of place, which was outputting incorrect results.

#Explain why you needed parentheses for the formula
#Parantheses are important for the order of operations. The program forces what is enclosed to run first.

#Top 3 things you have learned
#I learned about the round function, importance of order of operations, and the importance of proper naming conventions.

#Calculates future value of money compounded over time for given deposit, interest rate, compounding, and time.
#Ask user for deposit, interest rate, compounding, and time.
fPrincipalTY = float(input("Enter starting principal: "))
fAnnualInterestRateTY = float(input("Enter the annual interest rate: "))
fCompoundingTY = float(input("How many times a year is the interest compounded?: "))
fYearsTY = float(input("How many years will the account earn interest?: "))

#This converts the interest rate to a decimal
fAIRTY = fAnnualInterestRateTY / 100
#FV = PV(1+ r/m)**mt
#This is the formula used to calculate the interest rate
fFutureValueTY = fPrincipalTY * (1 + fAIRTY / fCompoundingTY)** (fYearsTY * fCompoundingTY)

#Display the results in a formatted manner.
#Utilizing the round() function to format the output result and make it more visually appealing.
print(f"At the end of {fYearsTY} years, you will have $", round(fFutureValueTY, 2))
