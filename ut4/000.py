from datetime import datetime as dt
from datetime import date
from datetime import timedelta

MAX_DATE = '2100-01-01'
MIN_DATE = '2000-01-01'
oneDay = timedelta(days=1)
date_now = dt.now().date()


def is_palindromo_date(date):
    strDate = str(date).replace('-', '')
    return strDate == strDate[:: -1]


def find_all_palindromo(current_date="2000-01-01", up=True):
    while str(current_date) != MIN_DATE and str(current_date) != MAX_DATE:
        if is_palindromo_date(current_date):
            print(current_date)
        if up:
            current_date += oneDay
        else:
            current_date -= oneDay


print('Past palindromes:')
find_all_palindromo(date_now, False)
date_now = date.today() + oneDay
print('Future palindromes:')
find_all_palindromo(date_now)
