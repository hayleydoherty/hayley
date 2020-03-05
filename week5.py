# Hayley Doherty
# Output whether today is weekday or not

a = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
import datetime

d = datetime.datetime.now()

# print(d.weekday())


if d.weekday() <= 4:
    print("it is a weekday")
else:
    print("it is the weekend")
