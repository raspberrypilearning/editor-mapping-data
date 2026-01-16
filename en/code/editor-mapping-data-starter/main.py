from p5 import *
from regions import get_region_coords
from random import randint

region_list = []
colours = {}


# Put code to run once here
def preload():
    pass


def setup():
    pass


# Put code to run when the mouse is pressed here
def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex


run()
