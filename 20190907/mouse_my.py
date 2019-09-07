day = 0
mouse_count = 2
# 쌀 100통 (쌀 한통 = 1KG = 1000g)
rice = 100 * 1000 

while rice > 0 :
    day += 1 # 하루가 지났다.
    rice = rice - 20 * mouse_count
    # print("쥐 {}마리가 쌀을 20g 씩 먹어서 {}만큼 먹고 {}가 남았다.".format(mouse_count, 20 * mouse_count, rice))
    if day % 10 == 0 :
        mouse_count *= 2
print("{}마리의 쥐가 {}일만에 다먹었다".format(mouse_count, day))
