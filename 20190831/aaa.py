a = input("첫번째 심판의 점수")
b = input("두번째 심판의 점수")
c = input("세번째 심판의 점수")
d = input("네번째 심판의 점수")
e = input("다섯번째 심판의 점수")

arr = [float(a), float(b), float(c), float(d), float(e)]
'''
max_score = arr[0]
min_score = arr[4]

if arr[1] >= max_score :
    max_score = arr[1]
elif arr[1] <= min_score :
    min_score = arr[1]

if arr[2] >= max_score :
    max_score = arr[2]
elif arr[2] <= min_score :
    min_score = arr[2]

if arr[3] >= max_score :
    max_score = arr[3]
elif arr[3] <= min_score :
    min_score = arr[3]

if arr[4] >= max_score :
    max_score = arr[4]
elif arr[4] <= min_score :
    min_score = arr[4]

print("최고 점수는 {}점이고, 최저점수는 {}점입니다.".format(max_score, min_score))

sum = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
'''

# len(arr) = 5
# 오름차순
i = 0
while i < len(arr) :
    if arr[i] > arr[i + 1] :
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    i += 1

# 최고, 최저 점수
max = arr[4]
min = arr[0]

# 합계
sum = arr[1] + arr[2] + arr[3]

avg = sum / 3
print(arr)
print(avg)



