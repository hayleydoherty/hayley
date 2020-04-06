# Hayley Doherty
# Output whether today is weekday or not

# a = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
import datetime                     # datetime is a module that is built in to python but you must import it from the library to use it

d = datetime.datetime.now()         # defining variable d as the currentdate and time using datetime

# print(d.weekday())


if d.weekday() <= 4:                # if statement used to determine if the day is between 1-4, Monday = 0, ... Friday = 4
    print("it is a weekday")        # if day is less than 4 (a weekday), this statement is printed
else:                               # else used to determine what to do if day is not less than 4, i.e. 5 or 6 thus being a weekend day
    print("it is the weekend")      # this statement is then printed
