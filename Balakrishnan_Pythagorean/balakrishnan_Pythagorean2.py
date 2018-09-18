leg1=input("enter a value for side a")
leg2=input("enter a value for side b")
leg3=input("enter a value for side c")

legOnesq=int(leg1)*int(leg1)
legTwosq=int(leg2)*int(leg2)
legThreesq=int(leg3)*int(leg3)

total_legOneandTwo = int(legOnesq)+int(legTwosq)

if int(leg1)+int(leg2) < int(leg3):
    print("not a right triangle")
elif int(leg1)+int(leg2) == int(leg3):
    print("IS a right triangle")
elif int(leg1)+int(leg2) < int(leg3):
    print("is an obtuse triangle")
elif int(leg1)+int(leg2) > int(leg3):
    print("is an acute triangle")
    
    
    
    