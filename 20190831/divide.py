print('수를 입력하세요: ')
a = int(input())

if a == 0 : 
    print("0은 나눗셈에 이용할 수 없습니다.")
    # sys.exit(0)  # 프로그램이 종료되지 않게
else :
    print('3 / ', a, ' = ', 3 / a)