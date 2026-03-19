#Snake Game for Middle School Student - Beginner Level

import turtle
import time 

delay = 0.1 #setting time otherwise snake is moving too fast off screen 

# Set up the screen
window = turtle.Screen()
window.title("Python Snake Simulator")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates, we will update the screen manually in our game loop

# Create the snake head
head = turtle.Turtle()
head.speed(0) #normal animation speed
head.shape("square")
head.color("white")
head.penup() #turtle was deisgned to draw lines when it moves, but we don't want that for our snake
head.goto(0, 0)
head.direction = "stop"

#Functions #for the four directions 
def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20) #for downward direction

    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20) #move alogn on the x-axis

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20) 

        #beginner friendly. - These functions could also be one line - head.sety(head.xcor()+20)



# Main game loop
while True:
    window.update()

    move() #calling the function 
    time.sleep(delay) #0.1 second - stops the program for 1/10th of a second 

    #up till here we have - screen 600 by 600 size, square snake and movement of the snake going up by 0.1 seconds. 


window.mainloop()

window.exitonclick() #allows the turtle pop up window to show up 


