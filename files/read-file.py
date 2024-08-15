"""
This example shows how file handlers are used to open, read, and close files.
"""
print("Here is my first file: \n")
f1 = open("/home/ec2-user/environment/files/files1.txt", "r")

print(f1.read())
f1.close()
print("\nNow lets create another file")
f2=open("/home/ec2-user/environment/files/files2.txt","w")
f2.write("This is All I want to tell you")
f2.close()
