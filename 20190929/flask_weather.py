from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)
@app.route("/")
def hello():
    # urlopen() 함수로 기상청의 정국 날씨를 읽습니다.
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # soup을 사용해 웹 페이지를 분석한다.
    soup = BeautifulSoup(target, "html.parser")

    # location 태그를 찾는다.
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력한다.
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
                )
        output += "<hr/>"
    return output

# cmd> set FLASK_APP=flask_weather.py
# cmd> flask run