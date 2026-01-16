<h2 class="c-project-heading--task">Load some data</h2>
--- task ---
Use the existing 'happy.csv' file
--- /task ---

Define a `load_data()` function to print the data in the file.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 27
line_highlights: 32-41
---
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
--- /code ---
</div>

Then call your function to use the happiness data file.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 15
line_highlights: 24
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

Click **Run** to see what your project should look like at this stage.
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

