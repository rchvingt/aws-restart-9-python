"""
Your module description
"""
print("Count to 10!")
for x in range(0,11):
    print(x)

#For every egg in a recipe, add 2 cups of flour
print("For every egg in a recipe, add 2 cups of flour")

flour=0
for egg in ["recipe1", "recipe2", "recipe3"]:
    flour+=2
    print(egg+" flour = "+str(flour))