"""
Use the if statement
Use the else statement
Use the elif statement
"""
print("Working with the if statement")
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply=='yes':
    print("We can help you ship that package!")
    
if userReply=='no':
    quit()
    
print("\n")
print("Working with the else statement")
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply=='yes':
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

print("\n")
print("Working with the elif statement")
userReply = input("Would you like to buy stamps, \nbuy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply=='stamps':
    print("We have many stamp designs to choose from")
elif userReply=='envelope':
    print("We have many envelope sizes to choose from.")
elif userReply=='copy':
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, please comeback again")