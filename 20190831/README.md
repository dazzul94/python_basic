# 2019-08-31

### - cmd 창에서 jupyter notebook > new Python3

### - 웹 사이트 띄우기
1. 사전작업: https://chromedriver.storage.googleapis.com/index.html 에서  
chrome://settings/help 내 크롬정보에 해당하는 압축파일을 다운로드 받는다.  
chromedriver.exe가 생긴다. 실행안해도 알아서 실행됨.(다운로드만 받으면 된다.)
2. 코드
>import webbrowser  

>url = 'www.google.com'  
>webbrowser.open(url)  

>%pwd 내경로

3. 네이버에서 검색하기   
메인페이지에서 검색버튼 누르면 나오는 url을 복사한다.

>import webbrowser  

>naver_search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="  
>search_word = "추석"  

>url = naver_search_url + search_word  

>webbrowser.open_new(url)  

4. 여러개의 사이트에서 띄우기(나중에 반복문으로)
- 네이버: 이천 반도체
- 다음: 이천 쌀
- 네이트: 이천 도자기
- 구글: 이천 복숭아

>import webbrowser  

>naver_search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="  
>naver_search_word = "이천 반도체"  

>daum_search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q="  
>daum_search_world = "이천 쌀"  

>nate_search_url = "https://search.daum.net/nate?thr=sbma&w=tot&q="  
>nate_search_word = "이천 도자기"   

>google_search_url = "www.google.com/#q="  
>google_search_word = "이천 복숭아"  

>url1 = naver_search_url + naver_search_word  
>url2 = daum_search_url + daum_search_world  
>url3 = nate_search_url + nate_search_word  
>url4 = google_search_url + google_search_word  

>webbrowser.open_new(url1)  
>webbrowser.open_new(url2)  
>webbrowser.open_new(url3)  
>webbrowser.open_new(url4) 

5. 리스트로 검색  
>import webbrowser  

>naver_search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="  
>naver_search_words = ['이천 반도체', '이천 쌀', '이천 도자기', '이천 복숭아']  
>for search in naver_search_words :  
>&nbsp;&nbsp;&nbsp;&nbsp;webbrowser.open_new(naver_search_url + search)  

6. 여러개의 사이트에 접속하기  
>import webbrowser  

>urls = ['www.naver.com', 'www.daum.net', 'www.nate.com']  
>for url in urls:  
>&nbsp;&nbsp;&nbsp;&nbsp;webbrowser.open_new(url)

7. 여러개의 사이트에 여러개의 검색어 

>import webbrowser    

>urls = ['https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=',   
'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=',   
'https://search.daum.net/nate?thr=sbma&w=tot&q=']   
>keywords = ['이천 반도체', '이천 쌀', '이천 도자기', '이천 복숭아']  
>for url in urls:   
>&nbsp;&nbsp;&nbsp;&nbsp;for key in keywords:  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;webbrowser.open_new(url + key)  

8. 여러개의 사이트에 각각의 검색어 띄우기

>import webbrowser   

>urls = ['https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=',  
'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=',  
'https://search.daum.net/nate?thr=sbma&w=tot&q=',  
'www.google.com/#q=']  
search_words = ['이천 반도체', '이천 쌀', '이천 도자기', '이천 복숭아']

>i = 0  
>for url in urls:  
>&nbsp;&nbsp;&nbsp;&nbsp;for word in search_words:  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if search_words[i] == word:  
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;webbrowser.open_new(url + word)  
>&nbsp;&nbsp;&nbsp;&nbsp;i += 1

### - 제어문
- 조건문: if
1. if
2. if ~ else
3. if ~ elif ~ else

- 반복문: for, while

### - 문자열 비교시 사전 순서대로 앞에 있는 것이 작은 값을 갖는다.
1. "가방" == "가방"  True  
2. "가방" != "하마" False
3. "가방" > "하마" False
4. "가방" < "하마" True



