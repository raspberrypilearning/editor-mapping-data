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
    # draw_pin(300, 300, Color(255, 0, 0))
    draw_data()


# Put code to run when the mouse is pressed here
def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex
    if pixel_colour in colours:
        facts = colours[pixel_colour]
        print(facts["name"])
        print(facts["happiness rank"])
        print(facts["happiness score"])
    else:
        print("Region not detected")


def load_data(file_name):
    with open(file_name) as f:
        for line in f:
            info = line.split(",")
            region_dict = {
                "name": info[0],
                "happiness rank": info[1],
                "happiness score": info[2],
            }
            # print(region_dict)
            region_list.append(region_dict)


def draw_pin(x, y, colour):
    no_stroke()
    fill(colour)
    ellipse(x, y, 10, 10)


def draw_data():
    red_value = 255
    for region in region_list:
        region_name = region["name"]  # Get the name of the region
        region_coords = get_region_coords(region_name)  # Get region coordinates
        region_x = region_coords["x"]  # Get the x coordinate
        region_y = region_coords["y"]  # Get the y coordinate
        region_colour = Color(red_value, 100, 0)  # Set the pin colour
        colours[region_colour.hex] = region
        draw_pin(region_x, region_y, region_colour)  # Draw the pin
        red_value -= 1


run()
