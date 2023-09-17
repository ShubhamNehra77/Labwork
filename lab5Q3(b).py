# Python Program to Print Mirrored Right Triangle Star Pattern

rows = int(input("Please Enter the Total Number of Rows  : "))

print("Mirrored Right Triangle Star Pattern")
i = 1
while(i <= rows):
    print(' ' * (rows - i) + '*' * i)
    i=i+1   
    