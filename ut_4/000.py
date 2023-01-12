import datetime
from datetime import datetime as dt
from datetime import date
from datetime import timedelta

MAX_DATE = datetime.date.fromisoformat('2100-01-01')
MIN_DATE = datetime.date.fromisoformat('2000-01-01')
ONE_DAY = timedelta(days=1)
date_now = dt.now().date()


def is_palindromo_date(fecha):
    str_date = str(fecha).replace('-', '')
    return str_date == str_date[:: -1]


def find_all_palindromo(current_date=datetime.date.fromisoformat("2000-01-01"), up=True):
    while current_date != MIN_DATE and current_date != MAX_DATE:
        if is_palindromo_date(current_date):
            print(current_date)
        if up:
            current_date += ONE_DAY
        else:
            current_date -= ONE_DAY


print('Past palindromes:')
find_all_palindromo(date_now, False)
date_now = date.today() + ONE_DAY
print('Future palindromes:')
find_all_palindromo(date_now)
