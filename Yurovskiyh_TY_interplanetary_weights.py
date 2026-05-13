#Coder: Timothy, Inter Planetary Weights
#Python3 Prof. Brian L. Candido

#1. What you liked about the assignment?
#I enjoyed applying everything that was taught.

#2. What you struggled with?
#I struggled with the formatting. I fixed it by lining up the curly braces.

#3. Explain specifically how you used Python formatting options to align the output
#I used the character spacing along with the "," seperator and .2f to limit the decimal to hundredths.

#Top 3 things you learned from this assignment: 
#CONSTANTS, conversions, and nested inputs within expressions.

#These are constants, which store the surface gravity factors for each planet.
MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

#Ask the user for their name and Earth weight.
sNameTY = input("Hello, what is your name? ")

#Using float data type to allow for decimal multiplication
fWeightTY = float(input("Please enter your Earth weight: "))

#Arithmetic operations
mercuryWeightTY = fWeightTY * MERCURY
venusWeightTY = fWeightTY * VENUS
moonWeightTY = fWeightTY * MOON
marsWeightTY = fWeightTY * MARS
jupiterWeightTY = fWeightTY * JUPITER
saturnWeightTY = fWeightTY * SATURN
uranusWeightTY = fWeightTY * URANUS
neptuneWeightTY = fWeightTY * NEPTUNE
plutoWeightTY = fWeightTY * PLUTO
#Calculate the users weight on each planet and the moon using provided gravity factors.

#Display the results in a formatted and aligned output that matches the sample exactly.
print(f"{sNameTY} your Earth weight on our Solar System's planets:")
print(f"{'Weight on Mercury:':10s} {mercuryWeightTY:10,.2f}")
print(f"{'Weight on Venus:':10s}   {venusWeightTY:10,.2f}")
print(f"{'Weight on the Moon:':10s}{moonWeightTY:10,.2f}")
print(f"{'Weight on Mars:':10s}    {marsWeightTY:10,.2f}")
print(f"{'Weight on Jupiter:':10s} {jupiterWeightTY:10,.2f}")
print(f"{'Weight on Saturn:':10s}  {saturnWeightTY:10,.2f}")
print(f"{'Weight on Uranus:':10s}  {uranusWeightTY:10,.2f}")
print(f"{'Weight on Neptune:':10s} {neptuneWeightTY:10,.2f}")
print(f"{'Weight on Pluto:':10s}   {plutoWeightTY:10,.2f}")


#Include CONSTANTS, variables, input, arithmetic operations, and output formatting.
