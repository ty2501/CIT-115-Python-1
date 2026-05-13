'''Timothy
Paint Calculator
Prof. C
What I liked about the assignment?
I liked coding the open() function for the file creation.
What I struggled with?
I struggled a bit with passing the correct parameters to the correct functions.
As a result there were improper readings initially.
What is a function?
It is a block of code made to do a specific task, and it can be reused all throughout the program.
It is useful when multiple values have to be processed in the same fashion.
Two reasons to code with functions: 1. Reduces redundancy.
2. Making changes to the program in the future becomes a lot easier.
'''
#math library for the math.ceil() function
import math

#data validation function
def getFloatInput(prompt):
    while True:
        try:
            inputValueTY = float(input(prompt))
            if inputValueTY > 0:
                return inputValueTY
            else:
                print("The number must be greater than 0")
        except ValueError:
            print("Invalid input - Please enter a numeric value")

#math functions, divide the area by the feet per gallon
def getGallonsOfPaint(sqFt, ftPerGal):
    return math.ceil(sqFt / ftPerGal)
#compute the total labor hours
def getLaborHours(laborHoursPerGallon, totalGallons):
    return laborHoursPerGallon * totalGallons
#compute the total labor cost
def getLaborCost(laborHours, laborCharge):
    return laborHours * laborCharge
#compute the total cost for the paint
def getPaintCost(totalGallons, paintPrice):
    return totalGallons * paintPrice

#tax function
def getSalesTax(tax):
    if tax == "CT":
        tax = 0.06
    elif tax == "MA":
        tax = 0.0625
    elif tax == "ME":
        tax = 0.085
    elif tax == "NH":
        tax = 0.0
    elif tax == "RI":
        tax = 0.07
    elif tax == "VT":
        tax = 0.06
    else:
        tax = 0
    return tax
#function which takes all required parameters from main()
def showCostEstimate(lastName, gallons, hours, paintCost, laborCost, taxAmount, total):
    #variable for the output filename
    filename = f"{lastName}_PaintJobOutput.txt"
    #open the file and write the following strings.
    with open(filename, "w") as file:
        file.write(f"Customer Last Name: {lastName}\n")
        file.write(f"Gallons of Paint: {gallons}\n")
        file.write(f"Hours of Labor: {hours:.1f}\n")
        file.write(f"Paint Charges: ${paintCost:,.2f}\n")
        file.write(f"Labor Charges: ${laborCost:,.2f}\n")
        file.write(f"Tax: ${taxAmount:,.2f}\n")
        file.write(f"Total Cost: ${total:,.2f}\n")
    #print the resulting output
    print(f"Gallons of paint: {gallons}")
    print(f"Hours of Labor: {hours:.1f}")
    print(f"Paint Charges: ${paintCost:,.2f}")
    print(f"Labor Charges: ${laborCost:,.2f}")
    print(f"Tax: ${taxAmount:,.2f}")
    print(f"Total Cost: ${total:,.2f}")
    print(f"File: {filename} was created.")
def main():
    #data input section
    fSqFtWallTY = getFloatInput("Enter wall space in square feet: ")
    fPaintPriceTY = getFloatInput("Enter the price of the paint per gallon: ")
    fFtpGalPaintTY = getFloatInput("Enter the feet per gallon of paint: ")
    fLaborHoursTY = getFloatInput("Enter the labor hours per gallon: ")
    fLaborChargeTY = getFloatInput("Enter the labor charge per hour: ")
    sStateTaxTY = input("Enter the state the job is in: ").upper() #capitalize all chars
    sLastNameTY = input("Enter your last name: ")

    #passes the requested variables to the functions to perform math calculations
    gallonsTY = getGallonsOfPaint(fSqFtWallTY, fFtpGalPaintTY)
    totalHoursTY = getLaborHours(fLaborHoursTY, gallonsTY)
    laborCostTY = getLaborCost(totalHoursTY, fLaborChargeTY)
    paintCostTY = getPaintCost(gallonsTY, fPaintPriceTY)

    #compute the sales tax
    salesTaxTY = getSalesTax(sStateTaxTY)
    taxAmount = (laborCostTY + paintCostTY) * salesTaxTY
    #add the computed sales tax to the total
    totalCostTY = laborCostTY + paintCostTY + taxAmount
    #invoke the cost estimate function. pass the user inputted parameters to the function
    showCostEstimate(sLastNameTY, gallonsTY, totalHoursTY, paintCostTY, laborCostTY, taxAmount, totalCostTY)

main()
