PI = 3.141592

# 숫자 입력 받기
def number_input():
    print("모듈의 __name__: " + __name__)
    output = input("숫자 입력> ")
    return float(output)

# 원주
def get_circumference(radius):
    return 2 * PI * radius

# 원의 넓이
def get_circle_area(radius):
    return PI * radius * radius