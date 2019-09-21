#랜덤으로 1000명의 키와 몸무게 만들기
import random

h_list = list("가나다라마바사아자차카타파하도레미파솔라시도민석")

with open("hanguls.txt",'w', encoding="UTF-8") as file:
    for i in range(1000):
        name = random.choice(h_list) + random.choice(h_list)
        weight = random.randrange(40, 100)
        height = random.randrange(160, 190)

        file.write("{},{},{}\n".format(name,weight,height))