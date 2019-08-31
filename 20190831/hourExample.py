import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("현재시간은 오전 {}시 {}분입니다".format(now.hour, now.minute))
else :
    print("현재시간은 오후 {}시 {}분입니다".format(now.hour, now.minute))