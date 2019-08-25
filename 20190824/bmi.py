'''
키, 몸무게를 입력받고 -> 키와 몸무게를 더한 값을 출력하라
몸무게(kg) ÷ (신장(m) × 신장(m))
'''

height = int(input("키를 입력해주세요.> "))
height = height / 100 #cm를 m로 변환

weight = float(input("몸무게를 입력해주세요.> "))

# bmi = weight / ( height * height )
bmi = weight / ( height ** 2 ) # 제곱 표현
print("당신의 BMI지수는 ", bmi, "입니다.")


if bmi < 18.5:
    print("당신은 저체중입니다.")
elif 18.5 <= bmi < 25.0:
    print("당신은 정상체중입니다.")
elif 25.0 <= bmi < 30:
    print("당신은 과체중입니다.")
elif 30 <= bmi:
    print("당신은 비만입니다.")
else:
    print("Error") 

