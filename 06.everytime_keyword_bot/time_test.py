import datetime

now = datetime.datetime.now()
pre = datetime.datetime(2018,9,8)
print(now)
print(pre)

print(now>pre) #최근 날짜가 더 큼
print(type(now))
print(type(pre))


test_date = "2018-09-07 18:58:09"
convert_date = datetime.datetime.strptime(test_date, "%Y-%m-%d %H:%M:%S")
print(convert_date)
print(type(convert_date))

print(now>convert_date)

three_minutes_later = convert_date+ datetime.timedelta(minutes=3)
print(three_minutes_later)