"""
Activity: Removing a user
"""

import os

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '"+username+"'? (Y/N)")
        confirm = input().upper()
    
    #Calls the Linux command sudo userdel -rwith the provided variable as the username
    os.system("sudo userdel -r "+ username)
    

remove_user()