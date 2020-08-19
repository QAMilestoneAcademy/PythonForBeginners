# print(dir(str))
#
# username = "Python3"
# print(username.lower())
##How you can write -Hello	Anu ! You are doing great !!I would also like to watch movie - Blah Blah ! I am just an year old to you:) my age is 3!!
your_name=input("Enter your Name :\t")
movie_name=input("Enter your favourite movie :\t")
your_age=int(input("Tell me how old are you?:\t"))

print("Hello {} ! You are doing great !!I would also like to watch movie - {} ! I am just an year old to you:) my age is {}!!".format(your_name.capitalize(),movie_name.title(),your_age+1))