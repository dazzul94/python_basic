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

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    scroe_average = score_sum / 4

    # 출력
    print(student["name"], score_sum, scroe_average, sep="\t")