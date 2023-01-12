from typing import Tuple, Dict, List


class Cell:
    def __init__(self):
        self.options = [i for i in range(1, 10)]
        self.location: Tuple[int, int, int] = (0, 0, 0)  # row, col, box
        self.row_cycles: Dict[int, List] = {}
        self.col_cycles: Dict[int, List] = {}
        self.box_cycles: Dict[int, List] = {}

    def remove_option(self, value: int):
        pass
