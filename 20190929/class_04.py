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

def student_get_sum(student):
    return student.korean + student.math + student.english + student.science
def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student.name,
        student_get_sum(student),
        student_get_average(student)
    )

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))