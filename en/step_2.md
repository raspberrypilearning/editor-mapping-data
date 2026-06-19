<h2 class="c-project-heading--task">Load some data</h2>

Use the existing 'happy.csv' file.

Define a `load_data()` function to print the data in the file.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 15-24
---
# Put code to run once here
def preload():
    global map
    map = load_image("old-map.jpg")


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
line_number_start: 27
line_highlights: 36
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

### Tip
<div class="c-project-callout c-project-callout--tip">
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

## Now run your code

Check what your project should look like at this stage.

<div class="c-project-output">
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-mapping-data-step-3" width="600" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
</div>
