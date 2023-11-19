import turtle as t
t.speed(0)
t.bgcolor("white")
t.pencolor("cyan")
t.pensize(0)
for a in range(155):
    t.rt(a)
    t.circle(125,a)
    t.fd(a)
    t.rt(90)
t.done()    
