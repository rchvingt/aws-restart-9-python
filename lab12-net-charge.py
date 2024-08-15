"""
Create a dictionary of pKa values (which indicate the strength of an acid) that will be used in the net charge calculations
Use the count() method to get a count of amino acids
Use a while loop to calculate the net charge of insulin from pH 0 to pH 14

"""
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpktz"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin
pKR = {
'y': 10.07,
'c': 8.18,
'k': 10.53,
'h': 6.00,
'r': 12.48,
'd': 3.65,
'e': 4.25
}
print(pKR)
print(type(pKR))

#Using count() to count the numbers of each amino acid
print("Using count() to count the numbers of each amino acid")
countY=insulin.count("y")
print(countY)
# floatY=float(insulin.count("Y"))
# print(floatY)
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

#Using count() to count the numbers of z in bInsulin
# seqCountZ = ({z: float(bInsulin.count(z)) for z in ['z']})
# print(seqCountZ)

print("Writing the net charge formula")
pH = 0
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1