"""
Demonstration: Static Debugging
"""
#python program with 2 errors
var = "Double value"
sumValue = var + 4

def doSomething(valueToCheck):
    if valueToCheck > 4:
        print("Bad indent")

doSomething(7)