<h2 class="c-project-heading--task">Draw the data pins</h2>

Place pins on the map to mark the regions at their coordinates.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

In the `load_data()` function, comment out the `print` and instead add each region in the dictionary to the region list.

Then define a `draw_data()` function that draws pins at each region's coordinates.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights:
---
            # print(region_dict)
            region_list.append(region_dict)


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
--- /code ---
</div>

In the setup function, comment out the `draw_pin` function and add a call to your new `draw_data` function.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 57
line_highlights:
---
    # draw_pin(300, 300, Color(255, 0, 0))
    draw_data()
--- /code ---
</div>

## Now run your code

Check what your project should look like at this stage.

<div class="c-project-output">
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-mapping-data-step-5" width="600" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
</div>
