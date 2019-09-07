from random import randint


'''
숫자와 자릿수가 맞으면 Strike, 
숫자는 맞지만 자릿수가 틀리면 Ball을 출력한다.
com  -> 2 5 8 
user -> 1 8 4
'''

# 1. 컴퓨터가 랜덤으로 네자리 숫자를 지정한다.
rn = ["0", "0", "0", "0"]
rn[0] = str(randint(1, 9))
rn[1] = str(randint(1, 9))
rn[2] = str(randint(1, 9))
rn[3] = str(randint(1, 9))

# 2. 네자리 숫자는 모두 다른 숫자여야만 하므로 중복되는 숫자를 제거한다.
while rn[0] == rn[1] :
    rn[1] = str(randint(1, 9))
while rn[1] == rn[2] or rn[2] == rn[0]:
    rn[2] = str(randint(1, 9))
while rn[2] == rn[3] or rn[3] == rn[0] or rn[3] == rn[1]:
    rn[3] = str(randint(1, 9))

print('rn=====', rn)
# 3. 변수 초기화
strike_cnt = 0
ball_cnt = 0
try_cnt = 0

print("=============================야구게임 시작==========================================")

while strike_cnt < 4 :
    user = input("네자리 숫자를 맞춰보아요")
    strike_cnt = 0
    ball_cnt = 0

    for i in range(0, 4) :
        for j in range(0, 4) :
            # strike조건: 자릿수가 같고 값도 같으면
            if user[i] == rn[j] and i == j : 
                strike_cnt += 1
            elif user[i] == rn[j] and i != j :
                ball_cnt += 1

    print("볼: {} 스트라이크: {}".format(ball_cnt, strike_cnt))
    try_cnt += 1

print("{} 번 만에 정답을 맞추었습니다.".format(try_cnt))

                



    




