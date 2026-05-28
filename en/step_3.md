<h2 class="c-project-heading--task">Add a pin</h2>

Your pin will be a single colour.

Create a function to draw a pin.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 27-30
---
            print(region_dict)


def draw_pin(x, y, colour):
    no_stroke()
    fill(colour)
    ellipse(x, y, 10, 10)

--- /code ---

</div>

Call your new function.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 33
line_highlights: 43
---
def setup():
    size(991, 768)
    image(
        map,  # The image to draw
        0,  # The x of the top-left corner
        0,  # The y of the top-left corner
        width,  # The width of the image
        height  # The height of the image
    )
    load_data('happy.csv')
    draw_pin(300, 300, Color(255,0,0))
--- /code ---
</div>

## Now run your code

Check what your project should look like at this stage. You will see one red pin (circle).
