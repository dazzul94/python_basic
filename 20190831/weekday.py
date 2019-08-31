'''
사용자로부터 요일을 입력받아 영문으로 출력
'''
weekday = input("요일을 입력하세요.> ")

if weekday == "월" :
    print("Monday")
elif weekday == "화" :
    print("Tuesday")
elif weekday == "수":
    print("Wednesday")
elif weekday == "목":
    print("Thursday")
elif weekday == "금":
    print("Friday")
elif weekday == "토":
    print("Saturday")
elif weekday == "일":
    print("Sunday")
else :
    print("잘못 입력하셨어요")