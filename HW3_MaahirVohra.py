#Maahir Vohra
#CS100 Section 008
#HW 02, February 6, 2023


import turtle
import math


##1
t = turtle.Turtle()
len = 100

#equilateral triangle, was going to do all of these w/ while loop but unsure if allowed to since we didn't learn it yet
t.forward(len)
t.left(120)
t.forward(len)
t.left(120)
t.forward(len)
t.left(120)

t.penup()
t.forward(150)
t.pendown()

#square
t.forward(len)
t.left(90)
t.forward(len)
t.left(90)
t.forward(len)
t.left(90)
t.forward(len)
t.left(90)

t.penup()
t.forward(150)
t.pendown()

#pentagon
t.forward(len)
t.left(72)
t.forward(len)
t.left(72)
t.forward(len)
t.left(72)
t.forward(len)
t.left(72)
t.forward(len)
t.left(72)

t.penup()
t.backward(500)
t.pendown()

##2
t.circle(50)

t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

t.circle(100)

t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

t.circle(150)

t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

t.circle(200)


##3
#a: 100!
print("#3A:", math.factorial(100))

#b: the log(base 2) of 1,000,000
print("#3B:", math.log2(1000000))

#c: the greatest common divisor of 63 and 49
print("#3C:", math.gcd(63, 49))