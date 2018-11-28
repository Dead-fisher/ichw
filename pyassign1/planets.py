# !/usr/bin/env python3

""" planets.py : description of trace of foobar.

__author__ = "Wang Yanze"
__pkuid__  = "1800011721"
__email__  = "1800011721@pku.edu.cn"
__phone__  = "18330873909"
"""

import turtle
import math

Sun = turtle.Turtle()
Venus = turtle.Turtle()
Mercury = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()

planets = [Venus, Mercury, Earth, Mars, Jupiter, Saturn, Sun]  # name of planets
color = ['black', 'purple', 'green', 'red', 'pink', 'blue', 'yellow']  # color of planets and their traces
major_axis = [380, 300, 260, 200, 140, 65, 0]  # major_axis of foobars' trace
minor_axis = [360, 260, 200, 180, 110, 60, 0]  # minor_axis of foobars' trace
rate = [0.5, 1, 1.5, 2, 2.5, 3]  # rate of the foobars


def set_planets(planet, color, a, b):
    """
   set a function to initialize the places of planets
   :param planet: name of planets
   :param color: color of planets and their traces
   :param a: major_axis
   :param b: minor_axis
   :return: None
    """
    planet.shape('circle')
    planet.speed(0)
    planet.color(color)
    planet.up()
    planet.goto(a - (a ** 2 - b ** 2) ** 0.5 + 100, 0)
    planet.down()


def draw_plants(planet, a, b, v, n):
    """
     set a function to draw the trace of ellipse by parametric equation
    :param a: major_axis
    :param b: major_axis
    :param v: rate
    :param n: angle of rotation
    :return: None
    """
    planet.goto(
        a * math.cos(math.radians(n * v)) - (a ** 2 - b ** 2) ** 0.5 + 100,
        b * math.sin(math.radians(n * v))
    )


def main():
    for i in range(7):
        set_planets(planets[i], color[i], major_axis[i], minor_axis[i])
    Sun.dot(50)  # Draw the sun at the focus of these ellipse.
    for i in range(10000):
        for x in range(6):
            draw_plants(planets[x], major_axis[x], minor_axis[x], rate[x], i)


if __name__ == '__main__':
    main()

turtle.done()
