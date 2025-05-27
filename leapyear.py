#init

#functions
def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100> 0:
        print(True)
    elif year % 400 >0:
        print(False)

#Main
is_leap_year(1900) #priint False
is_leap_year(2024) #print True
is_leap_year(2000) #print True
