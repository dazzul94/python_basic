# bmi = weight / (height /100) ** 2

name = input("이름을 입력하세요.> ")
height = int(input("키를 입력하세요.> "))
weight = int(input("몸무게를 입력하세요.> "))

print("{}님의 키는 {}cm이고 몸무게는 {}kg입니다.".format(name, height, weight))

bmi = weight / (height /100) ** 2

if 18.5 <= bmi < 23 :
    bmi_cd = "정상"
elif 23 <= bmi < 25 :
    bmi_cd = "과체중" 
elif 24 <= bmi < 30 :
    bmi_cd = "비만"
elif 30 < bmi :
    bmi_cd = "고도비만"
else : 
    bmi_cd = "저체중"

print("bmi 지수는 {}입니다. {}입니다.".format(bmi, bmi_cd))