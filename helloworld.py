"""
Uses for JSON
"""
import json

filename = 'userName.json'
name = ''

#Check for history file
try:
    with open(filename,"r") as r:
        #Load the user's name from file history'
        name = json.laod(r)
except IOError:
    print("First time login")

# If the user was found in the history file, welcome them back
if name != "":
    print("Welcome back, " + name + "!")
else:
    # If the history file doesn't exist, ask the user for their name
    name = input("Hello! What's your name? ")
    print("Welcome, " + name + "!")
    
# Save the user's name to the history file
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")