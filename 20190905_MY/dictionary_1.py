'''
- 딕셔너리
대응관계를 나타내는 자료형
연관배열(Associate array, Hash)
순차적이 아니라 Key 와 Value를 연결 - 마치 사전을 펼치듯
'''
d1 = {"name": "김다솔", "phone": "0349", "home": "yong-in"}
print(d1["name"])

d1["language"] = "python"

print(d1)

del d1["phone"]
print(d1)

# 키 리스트(keys())
keys = d1.keys()
print(keys)

# value 리스트(values())
print(d1.values())

# 아이템 리스트
print(d1.items())

# 키로 value 얻기 -> 존재하지 않는 키값일 때 none을 준다. 오류 발생하지 않음
print(d1.get("name"))

# 키로 value 얻기(get(key, nvl))
print(d1.get("key","없음"))

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in d1)

# 모두 지우기
d1.clear()
print(d1)