import tkinter as tk
root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

row_entry = tk.Entry(frame)
row_entry.pack()

col_entry = tk.Entry(frame)
col_entry.pack()


def create_grid():
    num_rows = int(row_entry.get())
    num_cols = int(col_entry.get())

    # Create the grid of boxes here
    canvas = tk.Canvas(frame, width=300, height=300)

    canvas.pack()

    box_size = 30

    for row in range(num_rows):
        for col in range(num_cols):
            x1 = col * box_size
            y1 = row * box_size
            x2 = x1 + box_size
            y2 = y1 + box_size

            canvas.create_rectangle(x1, y1, x2, y2)


create_button = tk.Button(frame, text="Create Grid", command=create_grid)
create_button.pack()

root.mainloop()

