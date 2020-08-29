#what_triangle
# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
while True:
    print("Input lengths of the triangle sides: ")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    if x+y>z and y+z >x and x+z>y:
        if x == y == z:
            print("Equilateral triangle")
        elif x==y or y==z or z==x:
            print("isosceles triangle")
        else:
            print("Scalene triangle")
    else:
        print("Enter correct measurement of sides. Bye for now !")
        break
