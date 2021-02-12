# Write a program that determine whether or not an integer input is a leap year.
# Definition of leap year:
# Rule 1: A year is called leap year if it is divisible by 400.

# Example: 1600, 2000 etc. are leap year while 1500, 1700 are not leap year.

# Rule 2: If year is not divisible by 400 as well as 100 but it is divisible by 4 then that year are also leap year.

# Example: 2004, 2008, 1012 are leap year.
def leapyear(year):
    if (year%400)==0 :
        print(year," -> ",True)
    elif (year%400)!=0 and (year%100)!=0 and (year%4)==0 :
        print(year," -> ",True)
    else:
        print(year," -> ",False)

leapyear(1600)
leapyear(2000)
leapyear(1500)
leapyear(2004)
leapyear(2008)
leapyear(2010)