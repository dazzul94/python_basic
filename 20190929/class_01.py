# 클래스(붕어빵틀) => 객체(붕어빵)

students = [
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "김다솔", "korean": 87, "math": 98, "english": 88, "science": 95},
]

# 학생을 한명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    scroe_average = score_sum / 4

    # 출력
    print(student["name"], score_sum, scroe_average, sep="\t")