import sys
from vacations_calendar import calendar
# Можна і не використовувати datetime :)
#from datetime import datetime

def check(date_str):
    date_check = date_str.split('/')
# Якщо на вхід функції прийшли некоректні дані
    if len(date_check) != 3:
        print("Error in function 'check()': invalid argument!")
        sys.exit()
# На той випадок якщо день або місяць будуть містити тільки один символ
    if len(date_check[0]) != 2:
        date_check[0] = '0' + date_check[0]
    if len(date_check[1]) != 2:
        date_check[1] = '0' + date_check[1]
    date_check_concat = date_check[0]+date_check[1]
    for key in calendar:
        if key == date_check_concat:
            return calendar[key]
    return None

#print(check('28/07/2020'))
