import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QGridLayout, QWidget
from PyQt5.QtGui import QBrush, QPen, QColor, QPainter, QPainterPath
from PyQt5.QtCore import Qt, QPointF, QRectF, QTimer


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
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


class MazeWidget(QGraphicsItem):
    def __init__(self, maze, cell_size):
        super().__init__()
        self.maze = maze
        self.cell_size = cell_size
        self.setZValue(-1)

    def boundingRect(self):
        return QRectF(0, 0, self.maze.width * self.cell_size, self.maze.height * self.cell_size)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(255, 255, 255), Qt.SolidPattern))
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if self.maze.grid[x][y] == 1:
                    painter.drawRect(
                        x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)


class MazeGUI(QMainWindow):
    def __init__(self, width, height, cell_size=20):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.maze = Maze(width, height)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        self.view.setSceneRect(
            0, 0, self.width * self.cell_size, self.height * self.cell_size)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setRenderHint(QPainter.Antialiasing, True)
        self.view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.widget = MazeWidget(self.maze, self.cell_size)
        self.scene.addItem(self.widget)
        self.setWindowTitle("Maze GUI")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

    def keyPressEvent(self, event):
        # Allow the user to regenerate the maze by pressing the space bar
        if event.key() == Qt.Key_Space:
            self.maze.generate_maze()
            self.widget = MazeWidget(self.maze, self.cell_size)
            self.scene.removeItem(self.scene.items()[0])
            self.scene.addItem(self.widget)
            self.view.setSceneRect(
                0, 0, self.width * self.cell_size, self.height * self.cell_size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MazeGUI(40, 30, 20)
    gui.show()
    sys.exit(app.exec_())
