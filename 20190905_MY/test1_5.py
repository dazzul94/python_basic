'''
a:b:c:d 문자열 replace로 a#b#c#d로 출력
'''
a = "a:b:c:d"
a = a.replace(":","#")
print(a)