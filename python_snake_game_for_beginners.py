#Snake Game for Middle School Student - Beginner Level
#Key componenets:
# 1. Head
# 2. Food
# 3. Segments
# 4. Collision with border 
# 5: Body Collisions 
# 6: Scoring 

import turtle
import time 
import random 

delay = 0.12 #setting time otherwise snake is moving too fast off screen 

#Score:
score = 0
high_score = 0
#when does score increase?:
#1. collision with food

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
food.shape("triangle")
food.color("red")
food.penup() #turtle was deisgned to draw lines when it moves, but we don't want that for our snake
food.goto(0, 100)

#create body for snake that grows as it eats food- list
segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0     High Score: 0", align = "center", font = ("Arial", 24, "normal"))




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

    # 4. Collision with boarder 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1) #pauses game
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segments:
        for segment in segments: #goes through list of segments 
            segment.goto(1000, 1000)

        #clear segment list - not just hide them 
        segments.clear()

        #Reset the score
        score = 0

        #Update the score display
        pen.clear() #avoids generic score and high score = 0 text and actual score and high score overlap
        pen.write("Score:  {}   High Score:   {}". format(score, high_score), align = "center", font = ("Arial", 24, "normal"))


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

        #increase the score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear() #avoids generic score and high score = 0 text and actual score and high score overlap
        pen.write("Score:  {}   High Score:   {}". format(score, high_score), align = "center", font = ("Arial", 24, "normal"))



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

    #5 - check for head collision with the body segments
    #if there is a collision with the segments, we sleep , go back to center, stop the head. hide all the segments and clear the segment list. 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the segments:
            for segment in segments:  
                segment.goto(1000, 1000)

            #clear segment list
            segments.clear()

            #Reset the score
            score = 0

            #Update the score display
            pen.clear() #avoids generic score and high score = 0 text and actual score and high score overlap
            pen.write("Score:  {}   High Score:   {}". format(score, high_score), align = "center", font = ("Arial", 24, "normal"))


    time.sleep(delay) #0.1 second - stops the program for 1/10th of a second 

    #up till here we have - screen 600 by 600 size, square snake and movement of the snake going up by 0.1 seconds. 


window.mainloop()


#window.exitonclick() #allows the turtle pop up window to show up 


