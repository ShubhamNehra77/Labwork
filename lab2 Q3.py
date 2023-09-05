x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
if (x<0 or y<0):
    print("invalid input")
elif (y%x==0):
    print("Divisible")
else:
    print("not divible")

