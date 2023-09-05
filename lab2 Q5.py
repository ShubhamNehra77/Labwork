#radius
radius=int(input("enter the radius"))
if radius>1 and radius<100:
    area=(22/7)*radius*radius
    print("area is:",area)
else:
    print("error")
    