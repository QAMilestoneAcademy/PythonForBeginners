# The for loop is commonly used to repeat some code a certain number of times. This is done by combining for loops with range objects.
for i in range(5):
  print("hello!")
for l in range(0,20,2):
    print(l)

# The range function creates a sequential list of numbers.
# The code below generates a list containing all of the integers, up to 10.
numbers = list(range(10))
print(numbers)

nums = list(range(5))
print(nums[4])


# If range is called with one argument, it produces an object with values from 0 to that argument.
# If it is called with two arguments, it produces values from the first to the second.

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

# range can have a third argument, which determines the interval of the sequence produced. This third argument must be an integer.
numbers = list(range(5, 20, 2))
print(numbers)