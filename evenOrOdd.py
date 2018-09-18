"""
Write a program that will take a number (Integers only) and
return a statement that will let the user know if it is even or odd
"""

x= float(input("enter a number"))

if (x%2==0):
    print ("this is an EVEN number")
    
elif (x%2==1):
    print ("this is an ODD number")
    
else:
    print ("this is NOT an integer")
