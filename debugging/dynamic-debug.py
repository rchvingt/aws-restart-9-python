"""
Demonstration: Dynamic Debugging
"""

#Ask the user for a value and confirm the supplied value is greater than 0

def checkValue(valueToCheck):
    assert (type(valueToCheck) is int), "You must enter a number."
    assert (valueToCheck > 0), "Value entered must be greater than 0"
    if valueToCheck > 4:
        print("Value is greater that 4")

var = int(input("Enter a number greater that 0: "))
checkValue(var)