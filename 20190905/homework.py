# 4자리 숫자 암호
# 중복x,연속x
def verify():
    pwd = input("4자리 숫자 암호 입력 해~")
    #print(len(pwd))

    if pwd.isnumeric() and len(pwd) == 4:
        p1 =int(pwd[0])
        p2 =int(pwd[1])
        p3 =int(pwd[2])
        p4 =int(pwd[3])
        pw = [p1, p2, p3, p4]
    else:
        print("4자리 숫자만 입력할 수 있습니다.")
        return False



    for idx, pw1 in enumerate(pw):
        for idx2, pw2 in enumerate(pw):
            #print(idx,pw1,"_",idx2,pw2)
            if idx != idx2:
                #print(idx,pw1,"_",idx2,pw2)
                if pw1 == pw2:
                    print("중복된 숫자 안돼.")
                    return False 
                #elif pw1+1 == pw2:
                #    print("연속된 숫자 안돼")
                #    return False
            if idx+1 == idx2:
                #print(pw1,"_",pw2)
                if pw1+1 == pw2 or pw1 == pw2+1:
                    print("연속된 숫자 안돼")
                    return False

    print("pass")
    return True                




# 실행해보자
verify()