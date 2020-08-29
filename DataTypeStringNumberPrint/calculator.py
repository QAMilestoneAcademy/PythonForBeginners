
while True:
    num1 = int(input("number1:\t"))
    num2 = int(input("number2:\t"))
    option = input("Please enter operation - add,multiply,divide,subtract:\t")
    if option=="add":
     print("add",num1+num2)
    elif option=="subtract":
     print("difference",num1-num2)
    elif option=="multiply":
     print("multiply",num1*num2)
    elif option=="divide":
     print("divide",num1/num2)
    else:
        print("type correct operation.")
        break