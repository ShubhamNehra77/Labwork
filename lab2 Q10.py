t=int(input("Enter a number :"))  
if t>=1 and t<=86400:
    h=t//3600
    t%=3600
    m=t//60
    t%=60
    print(h,"Hours ",m,"Minutes ",t,"Seconds")

else:
    print("invalid input")