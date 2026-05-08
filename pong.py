import turtle
import time

####SCREEN AND PADDLE SETUP####

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width = 300, height = 300)

#Left Paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid = 5, stretch_len =1) #tall and thin
left_paddle.penup()
left_paddle.goto(-350, 0)

#Right Paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0)

screen.tracer(0) #turns off automatic drawing 

####Moving the Paddles###

def left_paddle_w():
    left_paddle.sety(left_paddle.ycor() + 30)

def left_paddle_s():
    left_paddle.sety(left_paddle.ycor() - 30)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 30)

def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 30)

screen.listen()
screen.onkey(left_paddle_w, "w")
screen.onkey(left_paddle_s, "s")
screen.onkey(right_paddle_up, "Up")
screen.onkey(right_paddle_down, "Down")

###Ball###
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball_chx = 3 #how fast ball moves horizontally
ball_chy = 3 #how fast ball moves vertically

while True:
    screen.update()
    time.sleep(0.01)

    #Move the ball
    ball.setx(ball.xcor() + ball_chx)
    ball.sety(ball.ycor() + ball_chy)
    

#screen.mainloop() - replace with game loop

