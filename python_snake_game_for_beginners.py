#Snake Game for Middle School Student - Beginner Level
#Key componenets:
# 1. Head
# 2. Food
# 3. Segments


import turtle
import time 
import random 

delay = 0.12 #setting time otherwise snake is moving too fast off screen 

# Set up the screen
window = turtle.Screen()
window.title("Python Snake Simulator")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates, we will update the screen manually in our game loop

# Create the snake head
head = turtle.Turtle()
head.speed(0) #normal animation speed
head.shape("circle")
head.color("white")
head.penup() #turtle was deisgned to draw lines when it moves, but we don't want that for our snake
head.goto(0, 0)
head.direction = "stop"

#Create Food
food = turtle.Turtle()
food.speed(0) #normal animation speed
food.shape("circle")
food.color("red")
food.penup() #turtle was deisgned to draw lines when it moves, but we don't want that for our snake
food.goto(0, 100)

#create body for snake that grows as it eats food- list
segments = []


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
        head.setx(x+20) #move along on the x-axis

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20) 

        #beginner friendly. - These functions could also be one line - head.sety(head.xcor()+20)


#Functions to move the head
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"



#Keyboard actions - calling the functions to move the head
window.listen() #telling the window to listen for key-clicks
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")


# Main game loop
while True:
    window.update()

    #check for collision with the food
    if head.distance(food) < 20: #each of the basic turtle case is 20x20 so center is 10. If distance is less than 20 food and snake have collided 
        #move food to random spot 
        x = random.randint(-290, 290) #to prevent it going off the screen
        y = random.randint(-290, 290)
        food.goto(x,y) 

        #add segment for body
        new_segment = turtle.Turtle()
        new_segment.speed(0) #animation speed
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment) #append is a built in list method. Adds a single element to the end of an existing list. Here our list is segments. New_segment is being appended to Segment - allowing the body of the snake to "grow" in our game. 

    #Moving the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        #lets say I have ten segments. Length is 10. Lists however, start at 0-9. 10 -1 is 9. I can't go directly down to zero, will end up with 9 and 1+ which will lead me back to 1. I want to go down by 1 ach time. 
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is. Check if there is a segment that is more than 0. 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move() #calling the function - four directions on the axises
    time.sleep(delay) #0.1 second - stops the program for 1/10th of a second 

    #up till here we have - screen 600 by 600 size, square snake and movement of the snake going up by 0.1 seconds. 


window.mainloop()

#window.exitonclick() #allows the turtle pop up window to show up 


