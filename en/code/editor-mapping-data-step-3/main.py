#!/bin/python3
from p5 import *
from regions import get_region_coords
from random import randint

region_list = []
colours = {}


# Put code to run once here
def preload():
    global map
    map = load_image("old-map.jpg")


def setup():
    size(991, 768)
    image(
        map,  # The image to draw
        0,  # The x of the top-left corner
        0,  # The y of the top-left corner
        width,  # The width of the image
        height,  # The height of the image
    )
    load_data("happy.csv")


# Put code to run when the mouse is pressed here
def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex


def load_data(file_name):
    with open(file_name) as f:
        for line in f:
            info = line.split(",")
            region_dict = {
                "name": info[0],
                "happiness rank": info[1],
                "happiness score": info[2],
            }
            print(region_dict)


run()
