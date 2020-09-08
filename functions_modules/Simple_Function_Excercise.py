#Function to take name, age , address as argument and print information
def personal_details(name,age,address):
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

myname, myage = "Simon", 19
myaddress = "Bangalore, Karnataka, India"
personal_details(myname,myage,myaddress)