'''
다음과 같은 커피 메뉴가 있을 때 총 매출을 계산하는 프로그램을 작성하시오.
아메리카노: 2,000원
카페라떼: 3,000원
카푸치노: 3,500원
'''

ame = input("아메 몇잔 팔았니?")
latte = input("카페라떼 몇잔 팔았니?")
ccino = input("카푸치노 몇잔 팔았니?")

ame, latte, ccino = int(ame), int(latte), int(ccino)

print("총 매출은 {}원입니다".format( ame * 2000 + latte * 3000 + ccino * 3500 ) )