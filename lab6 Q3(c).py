epsilon =float(input("enter the value of epsilon error:"))
x=float(input("enter the value of X : "))
i=1
fact=1
F_i=x
fact=fact*((2*i+1)*(2*i))
F_i1=F_i - (x**(2*i+1))/fact

while abs(F_i1-F_i)>=epsilon:
    print(f"Iter{i} : ", abs(F_i1-F_i))
    F_i=F_i1
    i=i+1
    fact=fact*((2*i+1)*(2*i))
    if i % 2==0:
        F_i1=F_i1 + (x**(2*i+1))/fact
    else:
        F_i1=F_i1 - (x**(2*i+1))/fact

print("No. of terms: ", i+1)
print("F_i+1, F_i1")