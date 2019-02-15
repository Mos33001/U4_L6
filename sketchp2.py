from turtle import *

mos = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.setup(1000,800)
screen.title("Turtle Sketch")

mos.shape("turtle")
mos.pensize(2)
mos.color("#00e5ff")

def go_up():
	mos.setheading(90)
	mos.forward(10)
	
def go_down():
	mos.setheading(270)
	mos.forward(10)
	
def go_left():
	mos.setheading(180)
	mos.forward(10)
	  	
def go_right():
	mos.setheading(0)
	mos.forward(10)

def draw_square():
	for x in range(4):
		mos.forward(60)
		mos.left(90)

def draw_circle():
	mos.circle(25)

screen.onkey(go_left,"Left")
screen.onkey(go_right,"Right")
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
screen.onkey(draw_square, "s")
screen.onkey(draw_circle, "c")
screen.listen()

mainloop()