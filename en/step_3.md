<h2 class="c-project-heading--task">Load some data</h2>

<h2 class="c-project-heading--explainer">In this project you will make an interactive map that shows the happiness measures of different regions.</h2>

--- task ---

Define a `load_data()` function to take a `file_name` variable. Have your function open that file and `print()` out every line in it.

--- /task ---

Define a `load_data()` function to take a `file_name` variable and `print()` out every line in it.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 27
line_highlights: 31-34
---
# Put code to run when the mouse is pressed here
def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex

def load_data(file_name):
    with open(file_name) as f:
        for line in f:
            print(line)
--- /code ---
</div>

Then call your function to use the happiness data file.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 25
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
--- /code ---
</div>

--- task ---

Click **Run** to see what your project shoud look like at this stage.
--- /task ---
<div class="c-project-output">
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-mapping-data-step-3" width="600" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

The columns of the data are:

 - The name of the region
 - Where that region ranks in the world for average happiness
 - The average happiness score for the region

Here is an example of the data in this file:

```
Norway,1,7.537000179
Denmark,2,7.521999836
Iceland,3,7.504000187
```

</div>

