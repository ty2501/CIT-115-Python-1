#Timothy - Temperature Converter

#What did you like about this assignment?
#I liked utilizing the logical operators. (and & or)
#What did you struggle with?
#Initially, I struggled with the logical operators.
#I was getting similar output regardless of user input because capitalization was not addressed.
#Explain how an if else works; and how an if elif else works.
#An if else has 2 possible outcomes. The program verifies if a statement is True, and runs the else clause if not.
#An if elif else is similar, but with more outcomes. It is only limited to how many elifs are included.
#Which one did you code for this assignment? Why?
#I chose to use the if elif else because there were many variables at play. This minimizes potential problems that may occur due to incorrect user input.
#Top 3 things you learned from this assignment.
#Proper use of logical operators, user input validation, and making the input case insensitive.

#Ask user for input, whether it is in C or F,
#then converts it to the other scale using conditional logic
#if elif else. Program must validate user input, code logical/conditional statements,
#follow naming conventions taught in class. and display results formatted to one decimal place.

#Welcome message
print(f"Tim's Temperature Converter")

#Asks for user input and converts it to a float
fTemperatureTY = float(input("Input a temperature: "))

#Ask user for scale input
sScaleTY = input("Is this in Fahrenheit or Celsius?(F or C): ")

#Mathematical operations
fCelsiusTY = (5.0/9) * (fTemperatureTY - 32)
fFahrenheitTY = ((9.0/5.0) * fTemperatureTY) + 32

#Verify if user input is valid, and print the mathematical conversions in a formatted manner.
if sScaleTY == "F" or sScaleTY == "f" and fTemperatureTY > 212:
    print(f"Temperature cannot be > 212.")
elif sScaleTY == "F" or sScaleTY == "f":
    print(f"The Celsius equivalent is: {fCelsiusTY:.1f}")
elif sScaleTY == "C" or sScaleTY == "c" and fTemperatureTY > 100:
    print(f"Temperature cannot be > 100")
elif sScaleTY == "C" or sScaleTY == "c":
    print(f"The Fahrenheit equivalent is: {fFahrenheitTY:.1f}")
else:
    print(f"You must enter F or C.")
