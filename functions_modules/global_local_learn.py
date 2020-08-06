#global vs local variable
b=2 #global variable

# def show_num(name):
#     # b=2 #local variable
#     print("hello "+name)
#
# show_num("Anu")
#
# def show_age(age):
#     print("your age", age)

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)