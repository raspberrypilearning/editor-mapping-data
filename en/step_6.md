<h2 class="c-project-heading--task">Challenge</h2>

Change the map design.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

In the `preload()` function, change the map from "old-map.jpg" to "ink-map.jpg"

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 12
---
def preload():
    global map
    map = load_image("ink-map.jpg")
--- /code ---
</div>

## Now run your code

Check your new map.
