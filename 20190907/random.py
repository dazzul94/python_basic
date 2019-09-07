from random import randint

# randint : 입력 파라미터인 최소부터 최대까지 중 임의의 정수를 리턴한다
com = randint(1, 100)

count = 0

while True:
    user = int(input("1~100사이 정수입력> "))

    if com > user :
        print("UP")
        count += 1
    elif com < user :
        print("DOWN")
        count += 1
    else : 
        count += 1
        print("정답", count, "번에 맞추었습니다.")
        print("컴퓨터숫자는 {}이고, 유저는 {}을 입력했습니다.".format(com, user))
        break

