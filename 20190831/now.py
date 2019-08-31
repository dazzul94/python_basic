import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
print("%s년 %s월" %(now.year, now.month))