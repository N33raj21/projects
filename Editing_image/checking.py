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
    canvas.create_oval(x, y, x + 2, y + 2, fill='black', width=2)

def choose_pen_color():
    color = colorchooser.askcolor(title='Choose Pen Color')[1]
    canvas.bind('<B1-Motion>', draw)

root = tk.Tk()
root.title("Screenshot Editor")

canvas = tk.Canvas(root, width=800, height=900, bg='white')
canvas.pack()

# Load your screenshot image here (replace 'screenshot.png')
screenshot_image = tk.PhotoImage(file='image1.png')
canvas.create_image(0, 0, anchor='nw', image=screenshot_image)

# Add buttons for pen color selection and saving
pen_color_button = tk.Button(root, text='Choose Pen Color', command=choose_pen_color)
pen_color_button.pack()

save_button = tk.Button(root, text='Save', command=lambda: save_canvas(canvas, 'edited_screenshot.png'))
save_button.pack()

root.mainloop()
# plt.show()