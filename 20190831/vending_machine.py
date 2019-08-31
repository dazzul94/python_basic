money = int(input("돈을 넣어주세요.> "))

choice = input("선택) 1-사이다 2-콜라 3-물 > ")
if choice in '123' :
    if choice == "1" and money >= 700 :
        print("사이다가 나왔습니다. 덜컹 \n잔돈 {}원 반환합니다".format(money - 700))
    elif choice == "2" and money >= 800 :
        print("콜라가 나왔습니다. 덜컹 \n잔돈 {}원 반환합니다".format(money - 800))
    elif choice == "3" and money >= 1200 :
        print("물이 나왔습니다. \n잔돈 {}원 반환합니다".format(money - 1200))
    else :
        print("금액이 부족합니다.")
else :
    print("해당 음료가 없습니다.")
