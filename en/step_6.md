<h2 class="c-project-heading--task">Click to see the region's data</h2>
--- task ---
When the user clicks on a pin, the hex colour value of the pin is retrieved, and then the corresponding region is found in the dictionary.
--- /task ---

In your `mouse_pressed()` function, lookup the `pixel_colour` in the `colours` dictionary and print out the `region`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 30
line_highlights:
---
def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex
    if pixel_colour in colours:
        facts = colours[pixel_colour]
        print(facts['name'])
        print(facts['happiness rank'])
        print(facts['happiness score'])
    else:
        print('Region not detected')
--- /code ---
</div>

Define a `draw_data()` function that draws pins at each region's coordinates.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 60
line_highlights:
---
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

Then, in the setup function, comment out the `draw_pin` function and add a call to your new `draw_data` function.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights:
---
    # draw_pin(300, 300, Color(255, 0, 0))
    draw_data()
--- /code ---
</div>

--- task ---

Click **Run** to see your finished project should look like.
--- /task ---
<div class="c-project-output">
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-mapping-data-step-5" width="600" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
</div>

