import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab

def save_canvas(canvas, file_location):
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save(file_location)

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x , y, fill='orange', width=10)

def eraser(event):
    # Remove items within a small radius of the cursor
    x, y = event.x, event.y
    canvas.delete(tk.ALL)  # Delete all items (customize as needed)

def undo():
    if undo_stack:
        canvas_id = undo_stack.pop()
        canvas.delete(canvas_id)

def toggle_eraser():
    global erasing_mode
    erasing_mode = not erasing_mode
    if erasing_mode:
        canvas.bind('<B1-Motion>', eraser)
    else:
        canvas.bind('<B1-Motion>', draw)

root = tk.Tk()
root.title("Screenshot Editor")

canvas = tk.Canvas(root, width=1600, height=600, bg='white')
canvas.pack()

# Load your screenshot image here (replace 'screenshot.png')
screenshot_image = tk.PhotoImage(file='image1.png')
canvas.create_image(0, 0, anchor='nw', image=screenshot_image)

def choose_pen_color():
    color = colorchooser.askcolor(title='Choose Pen Color')
    canvas.bind('<B1-Motion>', draw)  # Bind the mouse motion event to the draw function


# Add buttons for pen color selection, saving, and eraser toggle
pen_color_button = tk.Button(root, text='Choose Pen Color', command=choose_pen_color)
pen_color_button.pack()

eraser_button = tk.Button(root, text='Eraser', command=toggle_eraser)
eraser_button.pack()

save_button = tk.Button(root, text='Save', command=lambda: save_canvas(canvas, 'edited_screenshot.png'))
save_button.pack()

erasing_mode = True  # Initialize erasing mode

undo_stack = []  # Initialize the undo stack

undo_button = tk.Button(root, text='Undo', command=undo)
undo_button.pack()

root.mainloop()
