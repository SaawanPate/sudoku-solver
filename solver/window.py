from PyQt6.QtGui import QPaintEvent
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout, QLineEdit, QStyle


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.resize(1000, 900)

        grid = QGridLayout()
        grid.setVerticalSpacing(0)
        grid.setHorizontalSpacing(0)
        for row in range(9):
            for col in range(9):
                cell = QLineEdit()
                # cell.
                grid.addWidget(cell, row, col)

        start_button = QPushButton("Start Solving")
        start_button.clicked.connect(self.start_solve)
        hlayout = QHBoxLayout()
        hlayout.addLayout(grid, 9)
        hlayout.addWidget(start_button, 1)

        self.setLayout(hlayout)

    def paintEvent(self, a0: QPaintEvent):
        self.setFixedHeight(int(9 / 10 * self.height()))

    def start_solve(self):
        pass
