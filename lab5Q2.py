#taking input from user
N=int(input("enter the number:"))
if N==0:
    print("enter a non zero number")
if N<0:
    print("enter a positive number")
i=1
while i<=1000:
    if i%N!=0:
        print(f'Numbers not divisible by N are \n {i}')
        
    else:
        i=i+1
        continue
    i=i+1

    
        
    


