import tkinter as tk
import random


class Maze:
    def __init__(self, width, height, cell_size=20):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[1 for y in range(height)] for x in range(width)]
        self.generate_maze()

    def generate_maze(self):
        # Start with a grid of walls
        self.grid = [[1 for y in range(self.height)]
                     for x in range(self.width)]
        # Choose a random starting point
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        # Carve the maze starting from this point
        self.carve_maze(x, y)

    def carve_maze(self, x, y):
        # Mark the current cell as visited
        self.grid[x][y] = 0
        # Get a random order to visit the neighbors
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(neighbors)
        # Visit each neighbor and carve a path to it if it hasn't been visited
        for nx, ny in neighbors:
            if nx < 0 or ny < 0 or nx >= self.width or ny >= self.height:
                continue
            if self.grid[nx][ny] == 1:
                self.grid[(x + nx) // 2][(y + ny) // 2] = 0
                self.carve_maze(nx, ny)


class MazeGUI:
    def __init__(self, width, height, cell_size=20):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.maze = Maze(width, height, cell_size)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(
            self.root, width=self.width * self.cell_size, height=self.height * self.cell_size)
        self.canvas.pack()
        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        for x in range(self.width):
            for y in range(self.height):
                if self.maze.grid[x][y] == 1:
                    self.canvas.create_rectangle(
                        x * self.cell_size, y * self.cell_size, (x + 1) * self.cell_size, (y + 1) * self.cell_size, fill="black")

    def run(self):
        self.root.mainloop()


maze_gui = MazeGUI(25, 25)
maze_gui.run()
