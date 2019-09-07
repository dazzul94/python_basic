from random import randint


'''
숫자와 자릿수가 맞으면 Strike, 
숫자는 맞지만 자릿수가 틀리면 Ball을 출력한다.
com  -> 2 5 8 
user -> 1 8 4
'''

# 1. 컴퓨터가 랜덤으로 세자리 숫자를 지정한다.
rn = ["0", "0", "0"]
rn[0] = str(randint(1, 9))
rn[1] = str(randint(1, 9))
rn[2] = str(randint(1, 9))

# 2. 세자리 숫자는 모두 다른 숫자여야만 하므로 중복되는 숫자를 제거한다.
while rn[0] == rn[1] :
    rn[1] = str(randint(1, 9))
while rn[1] == rn[2] or rn[2] == rn[0]:
    rn[2] = str(randint(1, 9))

# 3. 변수 초기화
strike_cnt = 0
ball_cnt = 0

print("=============================야구게임 시작==========================================")

# 4. 사용자에게 세자리 숫자를 받는다.
while True:
    number = input("세자리 숫자를 입력하세요. ")

    if number.isnumeric() and len(number) == 3 :
        nlist = [number[0], number[1], number[2]]

        for i in range(0, 3) :
            for j in range(0, 3) :
                # print(i, j)
                # 자릿수와 값이 같으면
                if rn[i] == nlist[j] and i == j :
                    strike_cnt += 1
                elif rn[i] == nlist[j] and i != j :
                    ball_cnt += 1
        print("{} Strike and {} Ball".format(strike_cnt, ball_cnt))
        
        if strike_cnt == 3 :
            print("3 Strike change!")
            break
    
    else : 
        print("세자리 숫자만 입력해주세요.")    


    




