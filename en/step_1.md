<h2 class="c-project-heading--task">Show the world map</h2>

Start by showing a map.

Create a global variable called 'map' and set it to load the 'old_map.jpg' image.

Replace `pass` in the `setup()` function with the canvas size and image data.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 11,12,16-23
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

### Tip
<div class="c-project-callout c-project-callout--tip">
- The canvas size is **991** pixels by **768** pixels.
</div>

## Now run your code

Check what your project should look like at this stage.

<div class="c-project-output">


<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-mapping-data-step-2" width="600" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
</div>
