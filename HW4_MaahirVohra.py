#Maahir Vohra
#CS100 Section 008
#HW 04, February 7, 2023
import turtle

##1
#a
a = 3
b = 4
c = 5

#b
if a < b:
    print("#1B:", "OK")

#c
if c < b:
    print("#1C:", "OK")

#d
if (a + b) == c:
    print("#1D:", "OK")

#e
if ((a**2) + (b**2)) == (c**2):
    print("#1E:", "OK")

'''________________________________________________________________________'''
##2
#b
if a < b:
    print("\n#2B:", "OK")
else:
    print("#2B:", "NOT OK")

#c
if c < b:
    print("#2C:", "OK")
else:
    print("#2C:", "NOT OK")

#d
if (a + b) == c:
    print("#2D:", "OK")
else:
    print("#2D:", "NOT OK")

#e
if ((a**2) + (b**2)) == (c**2):
    print("#2E:", "OK")
else:
    print("#2E:", "NOT OK")

'''________________________________________________________________________'''
##3
color = input("Please enter a color: ")
width = int(input("Please enter the line width: "))
length = int(input("Please enter the line length: "))
shape = input("Please choose a shape(line, triangle, or square): ")

t = turtle.Turtle()

if shape == "line" or shape == "Line":
    t.color(color)
    t.width(width)
    t.forward(length)
elif shape == "triangle" or shape == "Triangle":
    t.color(color)
    t.width(width)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
else: #assuming they are spelling it correctly, otherwise this would be elif and insert an else statement
    shape == "square" or shape == "Square"
    t.color(color)
    t.width(width)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)


