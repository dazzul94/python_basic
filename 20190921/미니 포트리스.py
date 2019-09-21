# 터틀 포트리스 게임
# 조작법 : spacebar = 발사, 화살표키 = 각도조절

import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)

    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))
    
    if d < 25:
        t.color("blue")
        t.write("성공", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("실패", False, "center", ("", 15))
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)


t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(50, 150)
t.pensize(10)
t.color("pink")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

t.color("pink")
t.up()
t.goto(-200, 10)
t.setheading(20)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()
t.mainloop()
