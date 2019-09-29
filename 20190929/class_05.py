# 클래스(붕어빵틀) => 객체(붕어빵)

# 클래스 선언
class Student:
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

students = [
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
    Student("김다솔", 90, 93, 49, 90),
]

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())