num = int(input("자연수를 입력해주세요"))

if num < 10 :
    print("한자리 수 입니다")
elif num < 100 :
    print("두자리 수 입니다.")
elif num < 1000 :
    print("세자리 수 입니다.")
else : 
    print("세자리 수 이상입니다.")
