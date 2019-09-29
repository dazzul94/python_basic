rice = 100 * 1000 # 쌀 100통 = 100 * 1000 (g)
mouse = 2
day = 0
while True:
    print("냠냠 =", rice, mouse, day)
    rice = rice - (mouse * 20)
    day += 1
    if day % 10 == 0:
        mouse *= 2
    if rice < 0:
        break
print(day, "만에 ", mouse, "마리의 쥐가 쌀을 다 먹어치웠다.")
