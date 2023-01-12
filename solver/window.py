from PyQt6.QtGui import QPaintEvent
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout

from solver.cell import Cell
from solver.line_edit import LineEdit
from solver.solver import Solver


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.setFixedSize(1000, 900)

        hlayout = QHBoxLayout()
        grid = QGridLayout()
        grid.setVerticalSpacing(0)
        grid.setHorizontalSpacing(0)

        start_button = QPushButton("Start Solving")
        start_button.clicked.connect(self.start_solve)

        hlayout.addLayout(grid, 9)
        hlayout.addWidget(start_button, 1)
        self.setLayout(hlayout)
        self.text_boxes = []
        for row in range(9):
            for col in range(9):
                text_box = LineEdit(row, col)
                text_box.setMinimumHeight(100)
                text_box.resize(100, 100)
                grid.addWidget(text_box, row, col)
                self.text_boxes.append(text_box)

    def start_solve(self):
        cells = []
        for text_box in self.text_boxes:
            text_box.given = True
            cell = Cell()
            if text_box.text() == "":
                text_box.given = False
            else:
                cell.options = [int(text_box.text())]
            cells.append(cell)
        solver = Solver()
        solver.solve()


