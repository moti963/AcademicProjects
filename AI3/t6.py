import numpy as np

# Take input of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Create a maze matrix
maze = np.zeros((rows, columns))

# Fill the borders of the maze with walls (1)
maze[0, :] = 1
maze[rows-1, :] = 1
maze[:, 0] = 1
maze[:, columns-1] = 1

# Print the maze matrix
print(maze)
