#!/usr/bin/env python3

"""
Stanford CS106A BabyGraphics GUI
built on babynames data
"""

import sys
import tkinter
import babynames


def make_gui(top, width, height, names):
    """
    (provided)
    Set up the GUI elements for Baby Names, returning the TK Canvas to use.
    top is TK root, width/height is canvas size, names is BabyNames dict.
    """
    # name entry field
    entry = tkinter.Entry(top, width=60, name='entry', borderwidth=2)
    entry.grid(row=0, columnspan=12, sticky='w')
    entry.focus()

    # canvas for drawing
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')
    canvas.grid(row=1, columnspan=12, sticky='w')

    space = tkinter.LabelFrame(top, width=10, height=10, borderwidth=0)
    space.grid(row=2, columnspan=12, sticky='w')

    # Search field etc. at the bottom
    label = tkinter.Label(top, text='Search:')
    label.grid(row=3, column=0, sticky='w')
    search_entry = tkinter.Entry(top, width=15, name='searchentry')
    search_entry.grid(row=3, column=1, sticky='w')
    search_out = tkinter.Text(top, height=3, width=70, name='searchout', borderwidth=2)
    search_out.grid(row=3, column=3, sticky='w')

    # When <return> key is hit in a text field .. connect to the handle_draw()
    # and handle_search() functions to do the work.
    entry.bind('<Return>', lambda event: handle_draw(entry, canvas, names))
    search_entry.bind('<Return>', lambda event: handle_search(search_entry, search_out, names))

    top.update()
    return canvas


def handle_draw(entry, canvas, names):
    """
    (provided)
    Called when <return> key hit in given text entry field.
    Gets search text, looks up names, calls draw_names()
    for those names to draw the results.
    """
    text = entry.get()
    lookups = text.split()
    draw_names(canvas, names, lookups)


def handle_search(search_entry, search_out, names):
    """
    (provided) Called for <return> key in lower search field.
    Calls babynames.search() and displays results in GUI.
    Gets search target from given search_entry, puts results
    in given search_out text area.
    """
    target = search_entry.get().strip()
    search_out.delete('1.0', tkinter.END)
    # GUI detail: by deleting always, but only putting in new text
    # if there is data .. hitting return on an empty field
    # lets the user clear the output.
    if target:
        # Call the search_names function in babynames.py
        result = babynames.search_names(names, target)
        out = ' '.join(result)
        #searchout = top.children['searchout']  # alt strategy to access fields
        search_out.insert('1.0', out)


# Provided constants to load and draw the baby data
FILENAMES = ['baby-1900.txt', 'baby-1910.txt', 'baby-1920.txt', 'baby-1930.txt',
             'baby-1940.txt', 'baby-1950.txt', 'baby-1960.txt', 'baby-1970.txt',
             'baby-1980.txt', 'baby-1990.txt', 'baby-2000.txt', 'baby-2010.txt']
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
SPACE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def year_index_x(width, year_index):
    """
    Given canvas width and year_index 0, 1, 2 .. into YEARS list,
    return the x value for the vertical line for that year.
    """
    # your code here
    sub_width = (width-SPACE-1)//len(YEARS)
    x_coord = sub_width * year_index
    return x_coord


def draw_fixed(canvas):
    """
    Erases the given canvas and draws the fixed lines on it.
    """
    canvas.delete('all')
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # your code here

    canvas.create_line(SPACE, SPACE, width - SPACE, SPACE)
    canvas.create_line(SPACE, height - SPACE, width - SPACE, height - SPACE)
    for year in range(len(YEARS)):
        canvas.create_line(SPACE + year_index_x(width, year), 0, SPACE + year_index_x(width, year), height)
        canvas.create_text(SPACE + year_index_x(width, year), height - SPACE, text=YEARS[year], anchor=tkinter.NW)


def draw_names(canvas, names, lookups):
    """
    Given canvas, names dict, lookups list of name strs,
    Draw the data for the lookups on the canvas.
    """
    draw_fixed(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # your code here
    count = 0
    for lookup in lookups:
        color = COLORS[count % 4]
        for year in range(len(YEARS)):
            name_dict = names[lookup]
            yr = YEARS[year]
            next_yr = yr + 10
            if yr in name_dict:
                y_index = names[lookup][yr]
            else:
                y_index = 1000
            if next_yr in name_dict:
                y_next_index = names[lookup][next_yr]
            elif next_yr not in name_dict:
                y_next_index = 1000
            x1 = SPACE + year_index_x(width-1, year)
            if next_yr <= 2010:
                x2 = x1 + (width-1) / len(YEARS)
            y1 = y_index/1000 * (height-(SPACE * 2)) + SPACE
            if next_yr <= 2010:
                y2 = y_next_index/1000 * (height-(SPACE * 2)) + SPACE
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            canvas.create_text(x1, y1, text=lookup + ' ' + str(y_index), anchor=tkinter.SW)
        count += 1
# main() code is provided


def main():
    args = sys.argv[1:]
    # Establish size - user can override
    width = 1000
    height = 600
    # Let command line override size of window
    if len(args) == 2:
        width = int(args[0])
        height = int(args[1])

    # Load data
    names = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = make_gui(top, width, height, names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
