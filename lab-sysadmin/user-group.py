"""
Activity: Adding a user to a group
"""
import os
import subprocess

def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")

    #Performs the groupscommand and saves the result to a variable, which is output later for the user to select from
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    
    #Takes the list of groups that the user should be added to
    print("ENter a list of groups to add the user to")
    print("The list should be separated by spaces, for example: \r\n group1 group2 group3")
    print("The available groups are:\r\n "+output.decode('utf-8'))
    chosenGroups = input("Groups: ")
    
    #Splits the string from the previous section into an array
    output = output.decode('utf-8').split(" ")
    
    #Splits the string from the previous section into an array
    chosenGroups = chosenGroups.split(" ")
    print("Add To: ")
    found = True
    groupString = ""
    
    #For each member of the chosenGroupsarrayIf the members exist in both groupsFor each member of the output arrayPrints whether the script createsa new group or usesan existing group when the user is added
    for grp in chosenGroups:
        #For each member of the output array
        for existingGrp in output:
            #If the members exist in both groups
            if grp == existingGrp:
                found = True
                print("- Existing Group: "+grp)
                groupString = groupString + grp + ","
        
        if found == False:
            #Prints whether the script createsa new group or usesan existing group when the user is added
            print("- New Group: "+grp)
            groupString = groupString + grp + ","
        else:
            found = False
            
    #Removes the final comma (,) and adds a space at the endof the line
    groupString = groupString[:-1]+" "
    confirm = ""
    
    #The whileloopends only if the user enters Y or N
    while confirm !="Y" and confirm !="N":
        print("Add user '"+username+"' to these groups? (Y/N)")
        
        #Takes user input and stores it in the variable confirm
        confirm = input().upper()
        
    if confirm == "N":
        print("User '"+"' not added")
    else:
        os.system("sudo usermod -aG "+groupString+username)
        
        #If the user entered Y, calls the Linux Command sudo usermod –aGwith the groups and the user that youcreated earlier
        print("User '"+username+"' added")
    
    
add_user_to_group()