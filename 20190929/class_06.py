# 클래스 선언
class Circle:
    # 생성자
    def __init__(self, radius):
        self.radius = radius

    def calcPerimeter(self):
        return self.radius * 2 * 3.14

    def calcArea(self):
        return self.radius * self.radius * 3.14

circle = Circle(100)
print("반지름: ", circle.radius,
    "원의 면적: ", circle.calcArea(),
    "원의 둘레: ", circle.calcPerimeter()   )