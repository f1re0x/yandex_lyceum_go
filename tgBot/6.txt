from turtle import *
lt(90)
size=20
screensize(2000,2000)
tracer(0)
down()
for i in range(9):
    fd(18*size)
    rt(72)
up()
for x in range(-20,30):
    for y in range(-20,30):
        setpos(x*size,y*size)
        dot(4,'red')
done()