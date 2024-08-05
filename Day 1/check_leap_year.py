

year = int(input('Enter a year :- '))


if (year%400 == 0) or (year%100 == 0) and (year%4 == 0):
    print("{} is a Leap Year".format(year))
else:
    print("{} is not a Leap Year".format(year))