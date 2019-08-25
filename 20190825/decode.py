'''
IP 확인 API로 접근해서 결과 출력하기
retrieve했던 이미지를 가져왔던 로그를 가져온다.

크롤링 할때 경각심을 가져야한다.
내가 접속했던 기록은 무조건 남는다.
''' 

# 모듈 읽어들이기
import urllib.request

# 데이터 읽어들이기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# 바이너리를 문자열로 변환하기
text = data.decode("utf-8")
print(text)