import turtle as t

side = 200
angle = 90

n = 20
n_angle = 360 / n
t.speed(0)

for i in range(n):
    for j in range(4):
        t.forward(side)
        t.right(angle)
    t.right(n_angle)

t.exitonclick()