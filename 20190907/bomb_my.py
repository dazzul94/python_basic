from random import randint

people = input("사용자 인원을 지정해주세요")
plist = []
# 사용자 번호지정
for i in range(0, int(people)) :
    plist.append(i + 1)
print(plist)

# 게임시작위치 선정
bomb_idx = int(input("게임시작위치를 지정(숫자 0 이상)"))
# 폭탄 넘기는 간격 선정
interval = int(input("폭탄 넘기는 간격 지정(숫자)"))

print("===================폭탄돌리기 시작=======================")

while len(plist) != 1 :
    bomb_idx = (bomb_idx + interval) % len(plist)
    plist.pop(bomb_idx)
    print("{}번 참가자가 아웃되었습니다.".format(bomb_idx))
    bomb_idx -= 1
print("최종생존자는 {}번 참가자입니다.").format(plist[bomb_idx])
    



