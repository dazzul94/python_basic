# 4자리 숫자 암호
# 중복x,연속x
def verify():
    input_pwd = input("4자리 숫자 암호를 입력하세요")

    if input_pwd.isnumeric() and len(input_pwd) == 4 :
        # 입력한 값이 모두 숫자이고 길이가 4이면 리스트에 담는다.
        pwd_list = [int(input_pwd[0]), int(input_pwd[1]), int(input_pwd[2]), int(input_pwd[3])]
    else :
        print("4자리 숫자만 입력해주세요")
        return False

    # 유효성 검사

    # enumerate: 인덱스와 요소 값을 반환
    for idx1, pwd1 in enumerate(pwd_list) :
        # print(idx1, pwd1)
        for idx2, pwd2 in enumerate(pwd_list) :
            # print(idx1, pwd1, "_", idx2, pwd2)
            if idx1 != idx2 and pwd1 == pwd2:
                print("중복된 숫자가 있습니다.")
                return False
            if idx1 + 1 == idx2 :
                if pwd1 + 1 == pwd2 or pwd1 == pwd2 :
                    print("연속된 숫자는 사용할 수 없습니다.")
                    return False

    print("사용할 수 있는 암호입니다.") 
    return True


# 실행해보자
if(verify() and input("정말 암호를 설정하시겠습니까?(y/n)") == 'y') :
    print("암호가 설정되었습니다!")
else : 
    print("암호를 다시 설정해주세요.")