# An if statement is run once if its condition evaluates to True, and never if it evaluates to False.
# A while statement is similar, except that it can be run more than once. The statements inside it are repeatedly executed, as long as the condition holds. Once it evaluates to False, the next section of code is executed.
# a=0
# while a<=5:
#     print("hello")
#     a+=1
# print("I am not in loop")

# How many numbers does this code print?
# i = 3
# while i>=0:
#    print(i)
#    i = i - 1


# The infinite loop is a special kind of while loop; it never stops running. Its condition always remains True.
# An example of an infinite loop:
# while 1 == 1:
#     print("In the loop")

#Fill in the blanks to create a loop that increments the value of x by 2 and prints the even values.
#
# x = 0
# while x <= 20:
#     print(x)
#     x += 2
# To end a while loop prematurely, the break statement can be used.
# When encountered inside a loop, the break statement causes the loop to finish immediately
# i = 0
# while 1==1:
#   print(i)
#   i = i + 1
#   if i >= 5:
#     print("Breaking")
#     break
# print("Finished")

#EXample:
# while True:
#     name=input("Enter your name: ")
#     print("hello" + name)
#
#     if(name==""):
#         print("bye! I need name")
#         break
# How many numbers does this code print?
# i = 5
# while True:
#   print(i)
#   i = i - 1
#   if i <= 2:
#     break
# Another statement that can be used within loops is continue.
# Unlike break, continue jumps back to the top of the loop, rather than stopping it
i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")
i=0
while i<=5:
  print("hello")
  i+=1

while True:
    num1 = int(input("enter num"))
    if num1==0:
        break
    print("hi")

