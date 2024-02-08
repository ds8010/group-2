"""Do not edit here"""

from turtle import Turtle, Screen


def pattern(turta,x,y,hexa_color, circle_color, square_color, border_color):
    """Creates a row of the pattrn in the order hexagon, circle and square from a given x and y coordinate."""
    setPos(turta,x,y)
    hexagon(turta,50,border_color,hexa_color)
    setPos(turta,x+150,y)
    circle(turta,50,border_color,circle_color)
    setPos(turta,x+225,y)
    square(turta,90,border_color,square_color)

def main():
    Hexa_color = input('Enter the color what you want to fill the hexagon with: ')
    Circle_color = input('Enter the color what you want to fill the circle with: ')
    Square_color = input('Enter the color what you want to fill the square with: ')
    Border_color = input('Enter the color what you want for the border of the shapes: ') 
    turta = Turtle()
    win = Screen()
    turta.speed(0)
    pattern(turta,-150,150,Hexa_color, Circle_color, Square_color,Border_color)
    pattern(turta,-50,20, Hexa_color,Circle_color,Square_color,Border_color)
    pattern(turta,50,-110,Hexa_color,Circle_color,Square_color,Border_color)
    win.exitonclick()

main()
