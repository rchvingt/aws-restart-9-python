"""
Use the list data type
Use the tuple data type
Use the dictionary data type___

"""
print("Defining a list")
myFruitList=["apple","banana","cherry"]
print(myFruitList)
print(type(myFruitList))

print("\n")
print("Accessing a list by position")

print("To access the apple string")
print(myFruitList[0])
print("\n")
print("To access the banana string")
print(myFruitList[1])
print("\n")
print("To access the cherry string")
print(myFruitList[2])
print("\n")
print("Changing the values in a list, from cherry to orange")
myFruitList[2]="orange"
print(myFruitList)
print(type(myFruitList))

print("Defining a tuple")
print("The tuple is like a list, but it can't be changed.\n A data type that can't be changed after it's created is said to be immutable.\n To define a tuple, you use parentheses () instead of brackets []")
print("\n")
myFinalAnswerTuple=("apple","banana","pineapple")
print(myFinalAnswerTuple)
print("\n")
print("In programming languages, the list position starts at zero (0)")

print("Accessing a tuple by position")
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print(type(myFinalAnswerTuple))

print("Defining a Dictionary")
print("A dictionary is a list with named positions (keys).\nImagine that your list shows people’s favorite fruit")
print("\n")
myFavoriteFruitDictionary={
    "Akua":"apple",
    "Saanvi":"banana",
    "Paulo":"pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("\n")
print("Accessing a dictionary by name")
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print("\n")
print("\n")
myFruitList=["apple","banana","cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFinalAnswerTuple=("apple","banana","pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary={
    "Akua":"apple",
    "Saanvi":"banana",
    "Paulo":"pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])