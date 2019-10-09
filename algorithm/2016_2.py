'''
각 사원의 아이디(ID), 등급(GD), 근무시간(TI)를 입력받아 사원들에 대한 주간급여(WAMT)
의 총합과 평균을 구하는 알고리즘이다.

<처리조건>
1. 사원의 주간급여(WAMT)는 근무시간(TI)와 시급(DAN)을 곱한 값으로 구한다.
2. 시급(DAN)은 사원의 등급(GD)이 
    1등급인 경우 10,000원,
    2등급인 경우 5,000원,
    3등급인 경우 2,000원으로 한다.
3. 근무시간이 36시간을 초과한 경우 초과근무시간에 대해 시급의 1.5배를 지급하며, 
근무시간(TI)은 최대 50시간까지만 인정한다.
4. 입력시 EOF가 입력되면 총합과 평균을 출력하고 종료한다. 
'''
wamt_sum = 0
wamt_avg = 0
id_count = 0

while True:
    id = input("사원 아이디를 입력하세요.> ")
    gd = int(input("등급을 입력하세요.> "))
    ti = int(input("근무시간을 입력하세요.> "))

    wamt = 0
    dan = 0 

    # 시급 dan set
    if gd == 1:
        dan = 10000
    elif gd == 2:
        dan = 5000
    elif gd == 3:
        dan = 2000

    if ti > 50:
        ti = 50

    if ti > 36:
        # 초과근무시간에 대해 시급의 1.5배
        wamt = (ti - 36) * dan
    else:
        wamt = ti * dan

    id_count += 1
    wamt_sum += wamt # 주간급여의 총 합

    wamt_avg = wamt_sum / id_count
    print("{} 님의 주간급여 WAMT는 {} 입니다.".format(id, wamt))
    print("지금까지의 총 주간급여의 합은 {}이고 평균은 {}입니다.".format(wamt_sum, wamt_avg))

    yn = input("그만 추가하시겠습니까? (Y/N)")
    if yn == "Y":
        break