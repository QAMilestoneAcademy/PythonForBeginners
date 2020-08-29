my_list=["paper","pen",2,"pencil"]


thislist = ["apple", "banana", "cherry"]

#len of list
print("lenght of list", len(thislist))

#access element
first_element=thislist[0]
last_element=thislist[len(thislist)-1]
print("my " + first_element)
print("my " + last_element)

##Add element to the list

new_element="orange"
thislist.append(new_element)
print(thislist)

##remove element to the list
thislist.remove("banana")
print(thislist)
my_empty_list=[]
##add a number to empty lis
my_empty_list.append(32)
print(my_empty_list)
my_empty_list.append(23)
print(my_empty_list)
#remove 23 from the list
my_empty_list.remove(23)
print(my_empty_list)

thislist_new = ["apple", "banana", "cherry"]

if "apple" in thislist_new and "banana" in thislist_new:
    print("apple and banana is there")
else:
    print("what is ")

