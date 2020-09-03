# # # empty dictionary
# my_dict = {}
#
# # # dictionary with integer keys
# my_dict = {1: 'apple', 2: 'ball'}
# #
# # # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}
# #
# # # using dict()
# # my_dict = dict({1:'apple', 2:'ball'})
# #
# # # from sequence having each item as a pair
# # my_dict = dict([(1,'apple'), (2,'ball')])
#
#
# #Access element
# student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
# print(student_grade["mahi"])
#
#
# # get vs [] for retrieving elements
person_detail = {'name': 'Jack', 'age': 26,'city':"Dubai"}

# Output: Jack
print(person_detail['name'])
print(person_detail['age'])
print(person_detail['city'])
#
person_detail['age']=27
print(person_detail)
#
# #remove element
student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
print(student_grade.pop("anay"))
# print(student_grade)
#
# ##add key value pair to the dictionary
# country_capital_dict={}
# country_capital_dict.update({"India":"Delhi"})
# print(country_capital_dict)
# country_capital_dict.update({"UAE":"Abudhabi"})
# print(country_capital_dict)

# #Find if key is in the dictionary
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# if 3 in d:
#   print('Key is present in the dictionary')
# else:
#   print('Key is not present in the dictionary')
student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
if "anu" in student_grade:
  print('Key is present in the dictionary')
else:
  print('Key is not present in the dictionary')

# # Iterate over dictionaries using for loops
# d = {'x': 10, 'y': 20, 'z': 30}
# d = {'x': 10, 'y': 20, 'z': 30}
#
# for element in d.items():
#     print(element)
#
# for dict_key, dict_value in d.items():
#     print(dict_key,'->',dict_value)
#
# # Generate and print a dictionary that contains a number in the form (x, x*x)
# n=int(input("Input a number "))
# d = dict()
#
# for x in range(1,n+1):
#     d[x]=x*x
#
# print("dictionary for first {} number & squares".format(n),d)
#
# # Python Program to multiply all the items in a dictionary.
#
# d={'A':10,'B':10,'C':239}
# tot=1
# for i in d:
#     tot=tot*d[i]
# print(tot)