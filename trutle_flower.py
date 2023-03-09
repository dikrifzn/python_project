import turtle
turtle.setworldcoordinates(-2000,-2000,2000,2000)
turtle.speed(10)
turtle.fillcolor('red')

turtle.begin_fill()
def draw_flower(x,y,tilt,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)

for tilt in range(0,360,30):
    draw_flower(0,0,tilt,1000)

turtle.end_fill()

turtle.mainloop() 