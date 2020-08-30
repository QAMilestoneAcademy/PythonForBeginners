# Define following variables & take them as user input
#
# name
# product
# unitprice
# totalMoney
# Find out the value of total quantities of product that can be brought with total money using : totalMoney//unitprice
#  Find out the money which would be left using : totalMoney%unitprice
# Make sure you convert numbers from inputstring to datatype int.
# print the output like below using string format:
# Hi anu.Your product is sofa.Price of each product is 200.You have total money 700.Hence you can bring 3 number of product sofa.You will be left with money 100
your_name=input("what is your name? \t")
name=input("what is the name of product? \t")
unitprice=float(input("what is the price of product? \t"))
total_money=float(input("How much money you have? \t"))
quantity_product=int(total_money//unitprice)
left_money=round(total_money%unitprice)
print(quantity_product)
print(left_money)
print()


