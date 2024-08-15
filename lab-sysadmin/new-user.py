"""
Activity: Working with Users
"""
import os

#Activity: Adding a user
def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: " )
        print("Use the username '"+username+"'? (Y/N)")
        confirm = input().upper()
    
    #Calls the Linux command sudo adduserwith the provided variable as the username
    os.system("sudo adduser "+username)
    
    
    
new_user()