#Define 3 numbers using variable .Find average of three numbers .

num1=3
num2=6
num3=5

sum_nums=num1+num2+num3
avg_num=sum_nums/3


###String operations
#Concatenation - joining strings
print("Spam" + 'eggs')

print("1"+"1")
##out of the way - concatenate number with string
#wrong-print("spam"+1+"egg")
print("spam"+ str(1)+"egg")

#Multiply strings

print("spam " * 3)

##What is the output of
print(3*'7')

##Using inplace operators
x = "spam"
print(x)

x += "eggs"
print(x)

y=int("3"+"4")
x=1
print(x+y)






#Tell Me about yourself

name = "James"  # type string
age = 12  # type int #Make sure before concatenating, you convert int type age to string using str(age)
fav_passtime = "I love to do coding"  # string with a sentence like "I love to do coding"
fav_movie = "Mission Impossible"  # string with one or multiple words
height_cm = 162.5  # data type float eg. 162.5 #Make sure before concatenating, you convert float type height_cm to string using str(height_cm)
fav_poem_2_lines = '''twinkle, twinkle little star
how I wonder what you are '''  # data type string with 2 lines;example; twinkle , twinkle little star #hint close string in triple quotes
# note \t is for giving tab or space between strings
# note \n is for new line character
about_myself = "My name is\t" + name + ".\n I am \t" + str(age) + "\t years old." + "\n My height is \t " + str(
   height_cm) + "\n" + fav_passtime + "\t in my free time." + "\n I love watching the movie - " + fav_movie + "\n Below are the 2 lines from my favourite poem:\n" + fav_poem_2_lines

print(about_myself)

