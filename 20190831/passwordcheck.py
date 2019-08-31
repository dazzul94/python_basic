'''
# 숫자 입력받는 법 1(스페이스바)
a, b, c, d = input("네개의 숫자입력").split()
print(a,b,c,d)
'''

'''
# 숫자 입력받는 법 2 
num = input("숫자 네개 입력: ")
print(num)
num1 = num[0]
num2 = num[1]
num3 = num[2]
num4 = num[3]
'''

num = input("숫자 네개 입력")


if len(num) != 4 :
    print("패스워드를 정수 4자리 숫자로 입력해주세요: ")
else :
    if num.isnumeric() :
        num1, num2, num3, num4 = int(num[0]), int(num[1]), int(num[2]), int(num[3])
        # print(num1, num2, num3, num4)

        # 중복되는 숫자 체크
        if (num1 == num2 or num1 == num3 or num1 == num4) \
        or (num2 == num3 or num2 == num4) \
        or (num3 == num4) :
            print("중복되는 숫자가 있어서 사용할 수 없는 암호입니다.")
        else : 
            if (num2 - num1) == (num3 - num2) == (num4 - num3) == 1 :
                print("하나씩 증가하는 형태이므로 사용할 수 없는 암호입니다.")
            elif (num1 - num2) == (num2 - num3) == (num3 - num4) == 1 :
                print("하나씩 감소하는 형태이므로 사용할 수 없는 암호입니다.")
            else :
                print("사용할 수 있는 암호입니다!!!")   
    else : 
        print("문자는 입력할 수 없습니다.")

