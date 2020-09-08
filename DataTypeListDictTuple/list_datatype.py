#List is a complex data type which is collection of different/same data types closed with square bracket.
# It can contain integer, float, string
student_details=["anu","agarwal",11,5.5]
#It can also contain list
student_details=["anu","agarwal",11,5.5,["red","yellow"]]

##Assignment on run, create some sample lists like number of 5 students,temperature over 5 days

##What can be done with list can be done with dir(list)
print(dir(list))

#Find the average of numbers in the list using sum and len functions

student_grade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
#Sum the numbers in list
print(sum(student_grade))



# x=input("Enter numbers separted by -").split("-")
# test_list = [int(i) for i in x]
# print(test_list)
#
# #Multiply
# result = 1
# for x in test_list:
#     result = result * x
# print(result)
#
# #Sum
# result = 0
# for x in test_list:
#     result = result+x
# print(result)


#find number of elements in the list
print(len(student_grade))

mean=sum(student_grade)/len(student_grade)
print(mean)
#find maximum value

print(max(student_grade))

#find number of students with grade 10.0
print(student_grade.count(10.0))

#Creating list with the help of range function
my_list=list(range(1,10))
print(list(range(1,10)))

##list of even numbers starting from zero to 20
my_list_even=list(range(0,21,2))
print(my_list_even)

##time to do looping
##append method
my_list_temp=[234,540,320,453]
my_list_finaltemp=[]

for temp in my_list_temp:
    my_list_finaltemp.append(temp/10)

print(my_list_finaltemp)

##above can be achieved with list comprehensions in one line
new_temps=[temp/10 for temp in my_list_temp ]
print(new_temps)

##List Comprehension with if

my_list_temp=[234,540,-999,320,453]
new_temps=[temp/10 for temp in my_list_temp if temp !=-999]

##Assignment - Define a function which takes list of mixed data of numbers & strings and returns list of only numbers
# my_list=[99,95,'no data',98,'no data',56]
# new_list=[ element for element in my_list if isinstance(element,str)==False]
# print(new_list)

my_list=[0,95,'no data',98,'no data',-56]
def foo(list_data):
 new_list=[ element for element in list_data if isinstance(element,str)==False]
 print(new_list)
foo(my_list)

##Assignment- From list of positive & negative integer, create a list with only positive integers using list comprehension
my_list=[1,2,-3,4,5,-9,-8]
def foo(list_data):
 new_list=[ element for element in list_data if element >0]
 print(new_list)
foo(my_list)


##Comprehension with if & else

my_list_temp=[234,540,-999,320,453]
new_temps=[temp/10 if temp !=-999 else 0 for temp in my_list_temp]
print(new_temps)



def foo(my_list):
 new_list = [float(temp) for temp in my_list]
 return sum(new_list)

my_list_temp=['1.2','2.6','3.3']
print(foo(my_list_temp))


# student_grade=[10,30.5,60,87]
# my_number_list=[10,7,6,5,4]
# my_sq_num_list=[]
#
# for num in my_number_list:
#     i=num**2
#     my_sq_num_list.append(i)


#
# # print(my_number_list)
# print(my_sq_num_list)

# my_str_number_list=['10','7','6','5','4']
# my_int_num_list=[]
# for num in my_str_number_list:
#     i=int(num)
#     my_int_num_list.append(i)
# print(my_int_num_list)
