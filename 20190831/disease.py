month = input("아이가 태어난지 몇개월입니까?> ")

month = int(month)

if month < 1 :
    print("결핵, B형간염 예방접종 대상자입니다.")
if month == 1 :
    print("B형간염 예방접종 대상자입니다.")
if 2 <= month <= 6 :
    print("파상풍, 폐렴구균 예방접종 대상자입니다.")
if 2 <= month <= 16 :
    print("폐렵구균 예방접종 대상자입니다.")