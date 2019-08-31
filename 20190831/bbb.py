num = input("점수 입력(스페이스바를 이용한다.) : ").split()

print(num)
runflag = True

if runflag : 
    mini = min(num)
    maxi = max(num)
    a, b, c, d, e = [float(x) for x in num]

    avg = (((a + b + c + d + e) - (float(mini) + float(maxi))) / 3)

    print(avg)