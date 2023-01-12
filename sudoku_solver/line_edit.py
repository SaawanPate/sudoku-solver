from PyQt6.QtCore import Qt, QLine
from PyQt6.QtGui import QPaintEvent, QPainter, QPen, QFont, QIntValidator
from PyQt6.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col
        self.given = False

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Arial", 20))
        self.setMaxLength(1)
        self.setValidator(QIntValidator())

    def paintEvent(self, a0: QPaintEvent):
        super().paintEvent(a0)
        painter = QPainter()
        painter.begin(self)
        thin_line = 2
        thick_line = 6
        painter.setPen(QPen(Qt.GlobalColor.black, thin_line, Qt.PenStyle.SolidLine))

        rect = self.rect()

        line = QLine(rect.topLeft(), rect.topRight())
        if self.row % 3 == 0:
            painter.setPen(QPen(Qt.GlobalColor.black, thick_line, Qt.PenStyle.SolidLine))
            painter.drawLine(line)
            painter.setPen(QPen(Qt.GlobalColor.black, thin_line, Qt.PenStyle.SolidLine))
        else:
            painter.drawLine(line)

        line = QLine(rect.topLeft(), rect.bottomLeft())
        if self.col % 3 == 0:
            painter.setPen(QPen(Qt.GlobalColor.black, thick_line, Qt.PenStyle.SolidLine))
            painter.drawLine(line)
            painter.setPen(QPen(Qt.GlobalColor.black, thin_line, Qt.PenStyle.SolidLine))
        else:
            painter.drawLine(line)

        painter.setPen(QPen(Qt.GlobalColor.black, thick_line, Qt.PenStyle.SolidLine))
        if self.row == 8:
            line = QLine(rect.bottomLeft(), rect.bottomRight())
            painter.drawLine(line)
        if self.col == 8:
            line = QLine(rect.topRight(), rect.bottomRight())
            painter.drawLine(line)
        painter.end()
