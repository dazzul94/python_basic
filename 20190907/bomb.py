from random import randint

people = input("사용자 인원을 지정해주세요")
plist = []
# 사용자 번호지정
for i in range(0, int(people)) :
    plist.append(i + 1)
print(plist)

bomb_idx = randint(1, int(people))
interval = randint(1, int(people))
print('bomb_idx===', bomb_idx)
print('interval ===', interval)

print("===================폭탄돌리기 시작=======================")

while len(plist) != 1 :
    bomb_idx = (bomb_idx + interval) % len(plist)
    plist.pop(bomb_idx)
    print("pop: ", bomb_idx)
    



