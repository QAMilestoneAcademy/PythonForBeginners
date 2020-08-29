# From a dictionary of films like below:
# film = {"Shrek": {"age": 3, "seats": 6},
#         "Mission Impossible 2": {"age": 5, "seats": 3},
#         "Endgame": {"age": 7, "seats": 5},
#         "Infinity War": {"age": 9, "seats": 5}}
# Let user choose the movie.Once user chooses movie, check if user has age eligibility to watch .If user fits age eligibility, check if seats are available.Let user enter valid number of seats and enjoy the movie.
film = {"Shrek": {"age": 3, "seats": 0},
       "Mission Impossible 2": {"age": 5, "seats": 3},
       "Endgame": {"age": 7, "seats": 5},
       "Infinity War": {"age": 9, "seats": 5}}
# print(film["Shrek"]["age"])
# print(film["Endgame"]["seats"])
# print(film["Infinity War"]["age"])

#
#

choice = input(
   "Which film would you like to watch? "
   "\n Shrek \n Mission Impossible 2 \n "
   "Endgame \n Infinity War "
   "\n Press enter to exit : ").strip().title()
# print(choice)
if choice in film:
   print(film[choice]["seats"])
   if film[choice]["seats"] == 0:
       print("sorry it is sold out \n")

   else:
       age = int(input("How old are you ? : ").strip())
#        if age >= film[choice]["age"]:
#            no_seats = film[choice]["seats"]
#            print("no seats left {} \n".format(no_seats))
#            a = int(input("Enter number of seats: "))
#            if no_seats > 0:
#                if a > no_seats:
#                    print("Enter less than or equal to the no of seats available !\n")
#                else:
#                    no_seats = no_seats - a
#                    film[choice]["seats"] = no_seats
#                    # print("no. of seats left {}: \n ".format(no_seats))
#                    print("Enjoyyyy the movie! \n")
#
#        else:
#            print("You are too young to see this movie ! Bye !\n")
#
# else:
#    print("Sorry this film does not exist in our list")
