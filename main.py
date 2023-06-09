import time
from datetime import datetime
from datetime import date


print('time.ctime() : ', time.ctime())  # 현재 시간

df = datetime(year=2023, month=5, day=5, hour=5, minute=5)
print('datetime : ', df, '| type(df) : ', type(df))
now_date = datetime.now()
print('datetime.now() : ', now_date)

d = date(year=2023, month=6, day=1)
print(d) #date만

today_date = date.today()
print(today_date)