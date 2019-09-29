# 클래스(붕어빵틀) => 객체(붕어빵)

# 클래스 선언
class Circle:
    # 생성자
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )