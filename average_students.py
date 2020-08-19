marks_students=input("Enter marks of  students separated by \"-\": \t")
#print(type(marks_students))
marks_students_list=marks_students.split("-")
print(marks_students_list)
print(type(marks_students_list))
#list comprehension
marks_students_list_int = [int(i) for i in marks_students_list ]
print(marks_students_list_int)


