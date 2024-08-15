"""
Activity: Handling packages
"""

def install_or_remove_package():
    iOrR = ""
    while iOrR != "I" and iOrR !="R":
        print("Would you like to install or remove package? (I/R)")
        iOrR = input().upper()

    #Checks whether the user wants to install or remove packages
    if iOrR == "I":
        iOrR = "install"
    else:
        iOrR = "remove"
    
    print("Enter a list of packages to install")
    
    #Describes how the input should be formatted
    print("The list should be separated by spaces, for example: ")
    print(" package1 package2 package3")
    print(" otherwise, input 'default' to "+iOrR+" the default packages listed in this program")
    
    package = input().lower()
    #Installsthe default list of packages for the script if the user specifies default
    if package == "default":
        package = defaultPackages
    
    if iOrR == "install
        #Calls the Linux command sudo apt-get installwith the packages that youspecified
        os.system("sudo apt-get install "+package)
    elif iOrR == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            
            #solutionChangesthe user input into uppercase so that it can be comparedCalls
            choice = input().upper()
            if choice == "Y":
                
                #Calls the Linux command sudo apt-get –-purge removewith the packages that youspecified
                os.system("sudo apt-get --purge "+iOrR+""+packages)
                break
            elif choice == "N":
                
                #Calls the Linux command sudo apt-get removewith the packages that you specified
                os.system("sudo apt-get "+iOrR+" "+packages)
                break

        #Calls the Linux command sudo apt autoremove,whichremoves any old package files (if they exist)
        os.system("sudo apt autoremove")
                
        
#Used together,these two Linux commands are a goodway tomaintain an up-to-date and clean environment. 
def clean_environment
    #Removes dependencies that were installed with applications and are no longer used by anything on the system
    os.system("sudo apt-get autoremove")
    
    #cleans obsolete deb-packages
    os.system("sudo apt-get autoclean")

def update_environment
    #Updates the package lists for packages that must beupgraded, and also for new packages that were recently added to the repositories
    os.system("sudo apt-get update")
   
    #Updates the current OS
    os.system("sudo apt-get upgrade")
    
    #Downloads and installs updates for all installed packages
    os.system("sudo apt-get dist-upgrade")