print("HELLO PYTHON STUDENTS")
print("HELLO PYTHON")
print('HELLO JAIPUR','HELLO RAJASTHAN','HELLO BRO')
x=5
print(x)
x=8
print(x)

a=3
b=7
c=a+b
print(a+b+c)
print(c)

a="HELLO"
b=" "
c="WORLD"

a=int(input("enter any number"))
print(a)

#addition , subtraction , multiplication , division

a=int(input("enter any number"))
b=int(input("enter number"))
print("additon",a+b)
print("subtraction",a-b)
print("multiplication", a*b)
print("division",a/b)

#average of numbers

a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
d=int(input("enter number"))
Avg=(a+b+c+d)/4
print("Average equals",Avg)

#Simple Interest

#Principal amount is
p=int(input("enter principal amount"))
#rate is
r=int(input("enter the rate"))
#time is
t=int(input("enter the time"))
#simple interest
Simple_Interest=(p*r*t)/100
#printing the output
print(Simple_Interest)

#finding speed
distance=int(input("enter distance (inKm):"))
time=int(input("enter time (in min):"))
#speed
speed=distance/time
#printing output
print(speed)


#area of traingle
#taking input
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#solving quadratic eqn
#taking input
a = float(input('Enter any number: '))
b = float(input('Enter any number: '))
c = float(input('enter any number: '))
# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
