# 클래스(붕어빵틀) => 객체(붕어빵)

# 클래스 선언
class Circle:
    # 생성자
    def __init__(self, radius):
        self.radius = radius

    def calcPerimeter(self):
        return self.radius * 2 * 3.14

    def calcArea(self):
        return self.radius * self.radius * 3.14