<h2 class="c-project-heading--task">Show the world map</h2>


--- task ---

Start by showing a map.

--- /task ---

Create a global variable called 'map' and set it to load the 'old_map.jpg' image.

Then set the canvas size in the `setup()` function.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 9,10,14-21
---
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
        height  # The height of the image
    )
--- /code ---
</div>

<div class="c-project-output">
--- task ---

Click **Run** to see what your project shoud look like at this stage.
--- /task ---
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-mapping-data-step-2" width="600" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

- The canvas size is **991** pixels by **768** pixels.

</div>

