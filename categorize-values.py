"""
Use numeric data types
Use string data types
Use the list data type
Use a for loop
Use the print() function

"""
print("You can mix data types in a Python list")
myMixedTypeList=[45,290578,1.02,True,"Hunden min er morsom.","45"]
print(myMixedTypeList)
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
