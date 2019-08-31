import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5 :
    print("봄입니다.")
elif 6 <= now.month <= 8 :
    print("여름입니다.")
elif 9 <= now.month <= 11 :
    print("가을입니다.")
else :
    print("겨울입니다.")
'''
elif 12 == now.month or 1 <= now.month <= 2 :
    print("겨울입니다.")
'''