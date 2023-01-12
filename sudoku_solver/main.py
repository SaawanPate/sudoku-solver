import sys

from PyQt6.QtWidgets import QApplication

from sudoku_solver.window import Window


def create_ui():
    pass


def create_cells():
    pass


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())



