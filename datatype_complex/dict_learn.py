# # empty dictionary
# my_dict = {}
#
# # dictionary with integer keys
# my_dict = {1: 'apple', 2: 'ball'}
#
# # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}
#
# # using dict()
# my_dict = dict({1:'apple', 2:'ball'})
#
# # from sequence having each item as a pair
# my_dict = dict([(1,'apple'), (2,'ball')])


#Access element
# student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
# print(student_grade["mahi"])


# get vs [] for retrieving elements
person_detail = {'name': 'Jack', 'age': 26,'city':"Dubai"}

# Output: Jack
print(person_detail['name'])
print(person_detail['age'])
print(person_detail['city'])

person_detail['age']=27
print(person_detail)

#remove element
student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
print(student_grade.pop("anay"))
print(student_grade)

##add key value pair to the dictionary
country_capital_dict={}
country_capital_dict.update({"India":"Delhi"})
print(country_capital_dict)
country_capital_dict.update({"UAE":"Abudhabi"})
print(country_capital_dict)



# # Output: 26
# print(my_dict.get('age'))
#
# # Trying to access keys which doesn't exist throws error
# # Output None
# print(my_dict.get('address'))
#
# # KeyError
# print(my_dict['address'])
#
#
# # Changing and adding Dictionary Elements
# my_dict = {'name': 'Jack', 'age': 26}
#
# # update value
# my_dict['age'] = 27
#
# #Output: {'age': 27, 'name': 'Jack'}
# print(my_dict)
#
# # add item
# my_dict['address'] = 'Downtown'
#
# # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
# print(my_dict)
#
#
# # Removing elements from a dictionary
#
# # create a dictionary
# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#
# # remove a particular item, returns its value
# # Output: 16
# print(squares.pop(4))
#
# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares)
#
# # remove an arbitrary item, return (key,value)
# # Output: (5, 25)
# print(squares.popitem())
#
# # Output: {1: 1, 2: 4, 3: 9}
# print(squares)
#
# # remove all items
# squares.clear()
#
# # Output: {}
# print(squares)
#
# # delete the dictionary itself
# del squares
#
# # Throws Error
# print(squares)
#
#
# # Dictionary Methods
# marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
#
# # Output: {'English': 0, 'Math': 0, 'Science': 0}
# print(marks)
#
# for item in marks.items():
#     print(item)
#
# # Output: ['English', 'Math', 'Science']
# print(list(sorted(marks.keys())))
