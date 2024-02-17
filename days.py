#Count the days between the dates

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countYears(day):
    years = day.year
    if (day.month <= 2):
        years -= 1
    
    # An year is a leap if is a multiple 4
    # Else : multiple 100
    return int(years/4) - int(years / 100) + int(years/400)

# Count the difference
def countDifference(date1, date2) :
    x1 = date1.year * 365 + date1.day

    for i in range(0, date1.month - 1):
        x1 += month_days[i]

    x1 += countYears(date1)

    x2 = date2.year * 365 + date2.day
    
    for i in range(0, date2.month - 1):
        x2 += month_days[i]

    x2 += countYears(date2)
    
    return (x2 - x1)

# declare the date
date1 = Date(int(input("Input your date: ")), int(input("input your month: ")), int(input("Input your year: ")))
date2 = Date(int(input("Input your date: ")), int(input("Input your month: ")), int(input("Input your year: ")))

print(countDifference(date1, date2), "days")

# from datetime import date

# fday = date(int(input("Input the year: ")), int(input("Input the month: ")), int(input("Input the date: ")))
# sday = date(int(input("Input the year: ")), int(input("Input the month: ")), int(input("Input the date: ")))


# dif = fday - sday
# print(f"There's {dif.days} days between {fday} and {sday}")