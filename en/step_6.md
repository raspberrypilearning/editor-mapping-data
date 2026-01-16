<h2 class="c-project-heading--task">Challenge</h2>
--- task ---
Change the map design.
--- /task ---

In the `preload()` function, change the map from "old-map.jpg" to "ink-map.jpg"

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 13
---
def preload():
    global map
    map = load_image("ink-map.jpg")
--- /code ---
</div>


--- task ---

Click **Run** to see your new map.
--- /task ---


