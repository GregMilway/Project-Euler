# count Sundays that fall on first of the month from 1/1/1901 to 31/12/2000
#start values
# Jan = 0, Feb = 1, Mar = 2, etc
# Sun = 0, Mon = 1, Tue = 2, etc
#1/1/1901 is Tuesday, thus 1901, 0, 2

year = 1901
month = 0
day = 2
new_day = 0
count_sundays = 0 #how many sunday 1st have we counted?

month_days = { 0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31 }

def get_month(n):
    return n%12

def is_leapyear(year):
    if not year%4:
        if not year%100:
            if not year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

while year < 2001: #we need to count up to Dec 31, 2000.
    for i in range(12):
        length = month_days[get_month(i)]
        if i == 1 and is_leapyear(year):
            length += 1
        new_day = (length%7 + day)%7
        if new_day == 0:
            count_sundays += 1
        day = new_day
    year += 1

print count_sundays
