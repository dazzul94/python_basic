'''
홍길동 씨의 평균점수
'''
score = {"국어": 80, "영어": 75, "수학": 55}
print("평균점수는 {}입니다".format( (score.get("국어") + score.get("영어") + score.get("수학") ) / 3))