# 폭탄돌리기
# 게임인원입력
# 1) players = input("게임참가인원: ").split()

players = ["김다솔1", "김다솔2", "김다솔3", "김다솔4", \
    "김다솔5", "김다솔6", "김다솔7", "김다솔8"]
print("이름출력:{}".format(players))

# 게임시작위치 선정
start = int(input("게임시작위치를 지정(숫자 0 이상)"))

# 폭탄 넘기는 간격 선정
step = int(input("폭탄 넘기는 간격 지정(숫자)"))

print("===============폭탄 돌리기 시작 ========================")
#플레이어가 한명 남을 때까지
while len(players) > 1 :
    drop = (start + step) % len(players)
    start = drop - 1
    print("{}번 참가자가 아웃되었습니다.".format(drop))
    del players[drop]
print("최종생존자는 {}입니다.".format(players))

