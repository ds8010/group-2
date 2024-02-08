"""Group: 2
   Author1:
   Part:

   Author2:hamad alsaadi 
   Part: contibuted with the square function and the setpos function, also the comments for the 2 functions.

   Author3:Dona Pal
   Part:Contributed with the hexagon and circle. Also helped with the comments. 

   Manifesto: This is a program is written to draw a hexagon, circle and square in a pattern in a row; and repeat the pattern two more times at different positions. """

from turtle import Turtle, Screen

def hexagon(turta,side_length,border_color,hexa_color):
    """Draws hexagon with a given side_lengh and a given border_color and fills it with a given hex_color."""
    turta.color(border_color)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.left(60)
    turta.forward(side_length)
    turta.end_fill()

def circle(turta,radius,border_color,circle_color):
    """Draws a circle with a given radius and a given border_color and fills it with a given circle_color."""
    turta.color(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(radius)
    turta.end_fill()

def square(turta,side_length,border_color,square_color):
    """Draws square with a give side_length and a given border_color and fills it with a given square_color."""
    turta.color(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(side_length)
    turta.left(90)
    turta.forward(side_length)
    turta.left(90)
    turta.forward(side_length)
    turta.left(90)
    turta.forward(side_length)
    turta.end_fill()


def setpos(turta,x,y): 
    """Sets the turtle to the given x and y coordinate value without any trace."""
    turta.setheadingheading(0)
    turta.penup()
    turta.goto(x,y)
    turta.pendown() 

