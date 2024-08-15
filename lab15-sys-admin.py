"""
Use os.system() to run a Bash command
Use subprocess.run() to run Bash commands
"""
import os
import subprocess


#Using os.system
#os.system("ls")
# os.listdir()
# os.mkdir("newFolder")
# os.listdir()
# os.rmdir("newFolder")
# os.listdir()
# os.getlogin()

#Using subprocess.run
# subprocess.run(["ls"])

#Using subprocess.run with two arguments
# subprocess.run(["ls","-l"])

#Using subprocess.run with three arguments
#subprocess.run(["ls","-l","README.md"])

#Retrieving system information
# command="uname"
# commandArgument="-a"
# print(f'gathering system information with command: {command} {commandArgument} ')
# subprocess.run([command,commandArgument])

#Retrieving information with command about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])