#!/usr/bin/env python
# coding: utf-8

# # Turtle
# 

# In[3]:


#Ex1
import turtle

turtle.shape("turtle")

for i in range(0, 5):
    turtle.forward(100)
    turtle.right(72)
    
turtle.exitonclick()


# In[5]:


#Ex2
import turtle

for i in range(10):
    turtle.right(36)
    for j in range(5):
        turtle.forward(100)
        turtle.right(72)
        
turtle.exitonclick()


# - scr = turtle.Screen()    #window 
# 
# - scr.bgcolor("yellow")    #set background color; default: white
# 
# - turtle.penup()    #remove pen even if turtle is moving
# 
# - turtle.pendown()    # put the pen on to draw a shape
# 
# - turtle.pensize(4)    
# 
# - turtle.shape("turtle")     #set a shape to "turtle"; default: triangle
# 
# - turtle.hideturtle()    #hide a turtle
# 
# - turtle.showturtle()
# 
# - turtle.begin_fill()    #fil the shape
# 
# - turtle.end_fill()
# 
# - turtle.color("black", "red")    #set a color inside of shape; in this case, black line and fill red color inside the shape
# 
# - turtle.exitonclick()    #close window automatically if click the turtle window
# 
# 
# 
# 

# In[13]:


#60
#draw a square

import turtle

turtle.shape("turtle")
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
    
turtle.exitonclick()


# In[19]:


#61
#draw a triangle
import turtle
turtle.begin_fill()
turtle.color("pink")
turtle.shape("turtle")

for i in range(0, 3):
    turtle.forward(100)
    turtle.right(120)
    
turtle.exitonclick()


# In[21]:


#62
#draw circle

import turtle
turtle.shape("turtle")

for i in range(360):
    turtle.forward(1)
    turtle.right(1)

turtle.exitonclick()


# In[25]:


#63
import turtle


turtle.begin_fill()
turtle.color("black", "red")

for i in range(0, 3):
    turtle.forward(40)
    turtle.right(120)
    
turtle.end_fill()    
turtle.penup()
turtle.forward(80)

turtle.pendown()
turtle.begin_fill()
turtle.color("black", "yellow")

for i in range(0, 3):
    turtle.forward(40)
    turtle.right(120)
turtle.end_fill()
    

turtle.penup()
turtle.forward(80)

turtle.pendown()
turtle.begin_fill()
turtle.color("black", "blue")

for i in range(0, 3):
    turtle.forward(40)
    turtle.right(120)
turtle.end_fill()    
turtle.exitonclick()


# In[33]:


#64
import turtle

for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()


# In[56]:


#65
import turtle

turtle.shape("turtle")

#1
turtle.left(90)
turtle.forward(100)
turtle.right(90)

turtle.penup()
turtle.forward(80)

#2
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)


turtle.penup()
turtle.forward(80)

#3
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.exitonclick()


# In[58]:


#66
import turtle
import random

turtle.pensize(3)

for i in range(0, 8):
    turtle.color(random.choice(["red", "yellow", "blue", "green", "orange", "pink"]))
    turtle.forward(50)
    turtle.right(45)
    
turtle.exitonclick()


# In[60]:


#67
import turtle

for i in range(10):
    for j in range(8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)
    
turtle.exitonclick()


# In[69]:


#68
import turtle
import random

lines = random.randint(5, 20)
for i in range(lines):
    length = random.randint(25,100)
    rotate = random.randint(1, 360)
    turtle.forward(length)
    turtle.right(rotate)
 

turtle.exitonclick()


# In[ ]:




