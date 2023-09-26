epsilon=float(input("enter the value of epsilon errors:"))
x=float(input("enter the value of x:"))
i=1
sum=0
while i<=epsilon:
    a=(1/2)**i
    sum=float(sum)+a
    i=i+1
print("Sum:",sum)