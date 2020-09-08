# What does the following code output?

x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less or Equal")
# What does the following code output?
#Note isinstance(variable_name) checks for variable type

x='2'
print(isinstance(x, int))
if isinstance(x, int) or isinstance(x, float) or x=='1':
    print("Valid type!")
else:
    print("Not valid!")

# What does the following code output?
def temp_verify(temp):
    if temp>25:
        return "Hot"
    elif temp >15 and temp <25:
        return "Warm"
    elif temp<=15:
        return "Cold"

today_temp=30

about_temp=temp_verify(today_temp)
print("Today's temperature is {}".format(about_temp))


# What does the following code output?

def verify_password(password):
    if len(password) < 8:
        print("Password less than 8 characters")
        return False
    else:
        print("Password  meets criteria")
        return True

my_password="anuradha"
verify_password(my_password)
