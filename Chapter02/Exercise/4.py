import turtle as t
for i in range(4):
    t.seth(i * 90)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0, 0)
    t.left(180)

t.done()