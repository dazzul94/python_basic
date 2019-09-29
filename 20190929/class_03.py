# 클래스(붕어빵틀) => 객체(붕어빵)

def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }
    
students = [
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90),
    create_student("김다솔", 90, 94, 95, 90)
]

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))