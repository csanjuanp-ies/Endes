from datetime import datetime as dt
from datetime import date
from datetime import timedelta

oneDay = timedelta(days=1)
currentDate = dt.now().date()


def IsPalindromoDate(date):
    strDate = str(date).replace('-', '')
    return strDate == strDate[: : -1]


print('Past palindromes:')
while str(currentDate) != '2000-01-01':
    if IsPalindromoDate(currentDate):
        print(currentDate)
    currentDate -= oneDay

currentDate = date.today() + oneDay
print('Future palindromes:')
while str(currentDate) != '2100-12-31':
    if IsPalindromoDate(currentDate):
        print(currentDate)
    currentDate += oneDay
