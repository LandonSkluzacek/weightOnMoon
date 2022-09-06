"""
Landon Skluzacek
9/2/2022

This code converts the weight on Earth to weight on the moon (in pounds).
"""
#Start of Code that asks weight on Earth.
weightOnEarth = float(input("Your weight on Earth: "))
#Converts weight on the Earth to weight on the moon.
weightOnMoon = int(weightOnEarth) * .165
#Prints weight in pounds on the moon.
print("Your weight on the moon is", weightOnMoon,"lbs")

"""
Landon Skluzacek
9/2/2022

This code converts the weight on Earth to weight on the moon (in pounds and ounces).
"""
#Start of Code that asks weight on Earth.
weightOnEarth = float(input("Your weight on Earth: "))
#Converts weight on the Earth to weight on the moon.
weightOnMoon = int(weightOnEarth) * .165
#This line takes just the decimal part and changes it to ounces.
ouncesOnMoon = (float(weightOnMoon) - int(weightOnMoon)) * 16
#Prints the answer in pounds and moon ounces.
print("Your weight on the moon is", int(weightOnMoon),"lbs", round(ouncesOnMoon), "ounces")

"""
Landon Skluzacek
9/2/2022

This code converts the weight on Earth to weight on the moon (kilograms).
"""

#Asks for weight in pounds
weightOnEarth = float(input("Your weight on Earth (in pounds): "))
#Converts to the weight on the moon.
weightOnMoon = int(weightOnEarth) * .165
#Converts new weight to kilos.
kilosOnMoon = weightOnMoon * 0.45359237
#Prints new weight in kilos and grams
print("Your weight on the moon is", kilosOnMoon, "kilos")

"""
Landon Skluzacek
9/2/2022

This code converts the weight on Earth to weight on Pythoid (kilograms and grams).
"""

#Asks for weight in pounds
weightOnEarth = float(input("Your weight on Earth (in pounds): "))
#Converts to the weight on the moon.
weightOnMoon = int(weightOnEarth) * .165
#Converts new weight to kilos.
kilosOnMoon = weightOnMoon * 0.45359237
#Finds the amount of grams.
gramsOnMoon = (float(kilosOnMoon) - int(kilosOnMoon)) * 1000
#Prints new weight in kilos and grams
print("Your weight on the moon is", int(kilosOnMoon), "kilos", round(gramsOnMoon), "grams")


"""
Landon Skluzacek
9/2/2022

This code converts the weight on Earth to weight on Pythoid (kilograms)
"""

#Asks for weight in pounds
weightOnEarth = float(input("Write your weight (in pounds): "))
#Start of equation
#Fraction part
fractionPartTop = ((weightOnEarth) ** 2 ) - 13
fractionPart = fractionPartTop / 8
additionPart = fractionPart + 22
squareRootPart = additionPart ** (1/2)
mulitplicationPart = 4 * squareRootPart

#Changes the name
weightOnPythoid = mulitplicationPart

#Print the weight on Pythoid
print("Your weight on Pythoid is ", weightOnPythoid, "pounds")

"""
Landon Skluzacek
9/2/2022

This code converts the weight on Earth to weight on Pythoid (kilograms and grams).
"""

#Asks for weight in pounds
weightOnEarth = float(input("Write your weight (in pounds): "))
#Start of equation
#Fraction part
fractionPartTop = ((weightOnEarth) ** 2 ) - 13
fractionPart = fractionPartTop / 8
additionPart = fractionPart + 22
squareRootPart = additionPart ** (1/2)
mulitplicationPart = 4 * squareRootPart

#Changes the name
weightOnPythoid = mulitplicationPart

ouncesOnPythoid = (float(weightOnPythoid) - int(weightOnPythoid)) * 16

#Print the weight on Pythoid
print("Your weight on Pythoid is ", int(weightOnPythoid), "pounds", round(ouncesOnPythoid), "ounces")






