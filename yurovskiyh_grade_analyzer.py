'''
Name: Timothy
Assignment: Grade Analyzer

What you liked about the assignment?
I liked troubleshooting the various problems I encountered.
What you struggled with?
Finding the lowest value.
I figured it out by comparing a starting value with the rest of them.
Then the lowest value is assigned to iLowestTY, which can be subtracted from iTotalTY
Top 3 things I learned:
    How to filter out a lowest value
    Use of raise SystemExit or exit() to halt the program
    There can be multiple ways to achieve the same outcome.
    In the end, I attempted to shorten the code.

'''
#Ask user for their name
sNameTY = input("Hello, what is your name? ")

#Ask user for 4 grades, whole numbers only
#Utilizing the try except to prevent non integers from being entered
try:
    iScore1TY = int(input("Enter in your first test score: "))
    iScore2TY = int(input("Enter in your second test score: "))
    iScore3TY = int(input("Enter in your third test score: "))
    iScore4TY = int(input("Enter in your fourth test score: "))
    #If statement to prevent negative values from being entered
    if iScore1TY < 0 or iScore2TY < 0 or iScore3TY < 0 or iScore4TY < 0:
        print("Test scores must be greater than zero.")
        exit()
except ValueError:
    print("Value must be a whole number.")
    exit()

#Ask user if lowest grade should be dropped; using upper() to capitalize the user input
sDropTY = input("Should your lowest grade be dropped?(Y)es or (N)o ").upper()

#If statement which prevents user from entering values which are not Y or N
if sDropTY != "Y" and sDropTY != "N":
    print("Enter Y or N")
    exit()

#Add up all values and store in iTotalTY
iTotalTY = iScore1TY + iScore2TY + iScore3TY + iScore4TY

#If statement to drop lowest grade, or not
if sDropTY == "Y":
    #Initialize lowest score, use if statements to find the lowest value
    iLowestTY = iScore1TY
    if iScore2TY < iLowestTY:
        iLowestTY = iScore2TY
    if iScore3TY < iLowestTY:
        iLowestTY = iScore3TY
    if iScore4TY < iLowestTY:
        iLowestTY = iScore4TY
    #Mathematical operations to find the average
    fAverageTY = (iTotalTY - iLowestTY) / 3
if sDropTY == "N":
    fAverageTY = iTotalTY / 4
    
#If statements to find the letter grade
if fAverageTY > 97:
    sLetterGradeTY = "A+"
elif fAverageTY >= 94:
    sLetterGradeTY = "A"
elif fAverageTY >= 90:
    sLetterGradeTY = "A-"
elif fAverageTY >= 87:
    sLetterGradeTY = "B+"
elif fAverageTY >= 84:
    sLetterGradeTY = "B"
elif fAverageTY >= 80:
    sLetterGradeTY = "B-"
elif fAverageTY >= 77:
    sLetterGradeTY = "C+"
elif fAverageTY >= 74:
    sLetterGradeTY = "C"
elif fAverageTY >= 70:
    sLetterGradeTY = "C-"
elif fAverageTY >= 67:
    sLetterGradeTY = "D+"
elif fAverageTY >= 64:
    sLetterGradeTY = "D"
elif fAverageTY >= 60:
    sLetterGradeTY = "D-"
elif fAverageTY <= 59.9:
    sLetterGradeTY = "F"

#Results, formatted
print(f"{sNameTY}, your test average is {fAverageTY:.1f}")
print(f"The letter grade is {sLetterGradeTY}")
