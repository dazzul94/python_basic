m100 = float(input("100m 기록(초)를 입력하세요. >"))
m1000 = float(input("1000m 기록(초)를 입력하세요. >"))
a = int(input("윗몸일으키기 기록(회)를 입력하세요. >"))
b = float(input("좌우 악력 기록(kg)를 입력하세요. >"))
c = int(input("팔굽혀펴기 기록(회)를 입력하세요. >"))

if m100 >= 13.6 \
   and m1000 >= 237 \
   and a >= 51 \
   and b >= 56 \
   and c >= 46 :
    print("합격 가능성이 매우 높습니다.")
else :
    print("합격 가능성이 낮습니다.")
