import tkinter as tk
from tkinter.colorchooser import askcolor


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.canvas_width = 500
        self.canvas_height = 500
        self.box_size = 50
        self.obstacle_color = None
        self.goal_color = None
        self.start_color = None
        self.obstacle_boxes = []
        self.goal_box = None
        self.start_box = None

    def create_canvas(self):
        self.canvas = tk.Canvas(
            root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.box_size
                y1 = row * self.box_size
                x2 = x1 + self.box_size
                y2 = y1 + self.box_size

                box = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white", outline="black")
                self.canvas.tag_bind(
                    box, "<Button-1>", lambda event, row=row, col=col: self.on_box_click(row, col))

    def on_box_click(self, row, col):
        color = self.get_selected_color()

        if color == self.obstacle_color:
            box = self.canvas.create_rectangle(col*self.box_size, row*self.box_size,
                                               (col+1)*self.box_size, (row+1) *
                                               self.box_size,
                                               fill=self.obstacle_color, outline="")
            self.obstacle_boxes.append(box)

        elif color == self.goal_color:
            if self.goal_box:
                self.canvas.delete(self.goal_box)
            self.goal_box = self.canvas.create_rectangle(col*self.box_size, row*self.box_size,
                                                         (col+1)*self.box_size, (row+1) *
                                                         self.box_size,
                                                         fill=self.goal_color, outline="")

        elif color == self.start_color:
            if self.start_box:
                self.canvas.delete(self.start_box)
            self.start_box = self.canvas.create_rectangle(col*self.box_size, row*self.box_size,
                                                          (col+1)*self.box_size, (row+1) *
                                                          self.box_size,
                                                          fill=self.start_color, outline="")

    def get_selected_color(self):
        if obstacle_var.get():
            return self.obstacle_color
        elif goal_var.get():
            return self.goal_color
        elif start_var.get():
            return self.start_color

    def choose_obstacle_color(self):
        color = askcolor()[1]
        self.obstacle_color = color
        obstacle_color_btn.config(bg=color)

    def choose_goal_color(self):
        color = askcolor()[1]
        self.goal_color = color
        goal_color_btn.config(bg=color)

    def choose_start_color(self):
        color = askcolor()[1]
        self.start_color = color
        start_color_btn.config(bg=color)


root = tk.Tk()

obstacle_var = tk.BooleanVar()
goal_var = tk.BooleanVar()
start_var = tk.BooleanVar()

obstacle_checkbox = tk.Checkbutton(
    root, text="Obstacle", variable=obstacle_var)
obstacle_checkbox.pack()

goal_checkbox = tk.Checkbutton(root, text="Goal", variable=goal_var)
goal_checkbox.pack()

start_checkbox = tk.Checkbutton(root, text="Start", variable=start_var)
start_checkbox.pack()

obstacle_color_btn = tk.Button(
    root, text="Choose Obstacle Color", command=lambda: grid.choose_obstacle_color())
obstacle_color_btn.pack()

goal_color_btn = tk.Button(
    root, text="Choose Goal Color", command=lambda: grid.choose_goal_color())

goal_color_btn.pack()

start_color_btn = tk.Button(
    root, text="Choose Start Color", command=lambda: grid.choose_start_color())
start_color_btn.pack()

rows_label = tk.Label(root, text="Rows:")
rows_label.pack()

rows_entry = tk.Entry(root)
rows_entry.pack()

cols_label = tk.Label(root, text="Columns:")
cols_label.pack()

cols_entry = tk.Entry(root)
cols_entry.pack()

create_grid_btn = tk.Button(
    root, text="Create Grid", command=lambda: create_grid())
create_grid_btn.pack()


def create_grid():
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    global grid
    grid = Grid(rows, cols)
    grid.create_canvas()


root.mainloop()
