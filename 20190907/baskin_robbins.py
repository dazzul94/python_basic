print("배스킨 라빈스 31 게임시작")

number = 1

while number < 31 :
    count = 0
    # 1번 플레이어
    while True :
        play1 = int(input("(0입력시 종료) 플레이어 1번 순서, 입력할 숫자는?"))

        if play1 == 0 : 
            print("0은 입력할수 없습니다.")
            break
        if play1 < number or play1 > number :
            print("잘못된 숫자를 입력했습니다. 다시 입력하세요.")
            count -= 1
            continue
        number = play1 + 1
        count += 1

    if count == 3 :
        print("")
    for i in range(number, 31 + 1) :
        print(i , end = ' ')
    print()

    # 2번 플레이어

    while True :
        play2 = int(input("(0입력시 종료) 플레이어 2번 순서, 입력할 숫자는?"))

        if play2 == 0 : 
            print("0은 입력할수 없습니다.")
            break
        if play2 < number or play2 > number :
            print("잘못된 숫자를 입력했습니다. 다시 입력하세요.")
            continue
        number = play2 + 1
    for i in range(number, 31 + 1) :
        print(i , end = ' ')
    print()

print("30 숫자를 외쳤습니다. 게임을 종료합니다. ")