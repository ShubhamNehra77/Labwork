m=int(input("Enter monthly installment amount in Rs. :"))
d=int(input("Enter the duration in months :"))
r=7.1
d=d/12
if m >= 500 and d >= 0.5:
    i=(m*d*r)/100
    print("Interest is ",round(i,2))
elif m<500:
    print("The monthly investment should be more than Rs.500")
elif d<0.5:
    print("The duration shoud atleast be 6 months")
else:
    print("Invalid input")

