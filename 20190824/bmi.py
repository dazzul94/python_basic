'''
키, 몸무게를 입력받고 -> 키와 몸무게를 더한 값을 출력하라
몸무게(kg) ÷ (신장(m) × 신장(m))
'''

height = int(input("키를 입력해주세요.> "))
print("height==", height / 100)

weight = float(input("몸무게를 입력해주세요.> "))
print("weight==", weight)

bmi = weight / height * height / 100
print("bmi==", bmi)


'''
if True:
    print("트루!")
'''

