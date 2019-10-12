'''
사원 N명에 대한 입사점수 중 최고점수와 최저점수를 뺀 점수의 합계와 평균
N: 입력자료갯수, P:카운터, MAX:최대값, MIN:최소값, JUM:점수, HAP: 합, AVG: 평균
'''
hap = 0
avg = 0
p = 0

min = 100000
max = 0

n = int(input("전체 사원의 명수를 입력하세요.> "))

while True:
    jum = int(input("사원의 점수를 입력하세요.> "))
    p += 1

    hap = hap + jum 

    if max < jum:
        max = jum
    if min > jum:
        min = jum

    if p >= n:
        break
hap = hap-(max + min)
avg = hap / (n - 2)
print("전체 사원의 최고점수, 최저점수를 뺀 합계는 {}이고 평균은 {}입니다.".format(hap, avg))
