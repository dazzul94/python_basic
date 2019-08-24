'''
당신의 나이는 몇 살입니까?

당신은 30 년을 살았습니다. 

아하~ 당신은 몇년도에 태어나셨군요

'''

from datetime import datetime 
now = datetime.now() 

my_age = int(input("당신의 나이는 몇 살입니까?"))

print("당신은 ", my_age, " 년을 살았습니다.")

print("아하~ 당신은 ", now.year + 1 - my_age, "년도에 태어나셨군용")


