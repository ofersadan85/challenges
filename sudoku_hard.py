from itertools import product
import numpy as np

boxes = slice(0, 3), slice(3, 6), slice(6, 9)
boxes = list(product(boxes, boxes))


class Cell:
    def __init__(self, x: int, y: int, value: int = 0) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.possibilities = set(range(1, 10))
        self.box = slice(x // 3 * 3, x // 3 * 3 + 3), slice(y // 3 * 3, y // 3 * 3 + 3)


class Sudoku:
    def __init__(self, values: list[list[int]]) -> None:
        self.cells = np.zeros((9, 9), dtype=object)
        self._entropy = np.zeros((9, 9), dtype=int)
        self._entropy.fill(9)
        for y, x in product(range(9), range(9)):
            cell = Cell(x, y, values[y][x])
            if values[y][x] != 0:
                cell.possibilities = set()
            self.cells[y, x] = cell
        self.reduce_entropy()

    def reduce_entropy(self) -> None:
        for cell in self.cells.flat:
            if cell.value == 0:
                cell.possibilities -= {cell.value for cell in self.cells[:, cell.x]}
                cell.possibilities -= {cell.value for cell in self.cells[cell.y, :]}
                cell.possibilities -= {
                    cell.value for cell in self.cells[cell.box[1], cell.box[0]].flat
                }

    def entropy(self) -> np.ndarray:
        return np.array(
            [[len(cell.possibilities) for cell in row] for row in self.cells]
        )

    def collapse(self) -> None:
        changed = True
        while changed:
            changed = False
            for cell in self.cells.flat:
                if cell.value == 0 and len(cell.possibilities) == 1:
                    cell.value = cell.possibilities.pop()
                    cell.possibilities = set()
                    changed = True
            self.reduce_entropy()

    def enforce_rows(self, checked: int) -> None:
        allowed = []
        for row in self.cells:
            for cell in row:
                if checked in cell.possibilities:
                    allowed.append(cell)
        if len(allowed) == 1:
            allowed[0].value = checked
            allowed[0].possibilities = set()
            self.reduce_entropy()

    def enforce_columns(self, checked: int) -> None:
        allowed = []
        for column in self.cells.T:
            for cell in column:
                if checked in cell.possibilities:
                    allowed.append(cell)
        if len(allowed) == 1:
            allowed[0].value = checked
            allowed[0].possibilities = set()
            self.reduce_entropy()

    def enforce_boxes(self, checked: int) -> None:
        allowed = []
        for box in boxes:
            cells = self.cells[box[0], box[1]].flat
            for cell in cells:
                if checked in cell.possibilities:
                    allowed.append(cell)
        if len(allowed) == 1:
            allowed[0].value = checked
            allowed[0].possibilities = set()
            self.reduce_entropy()

    def enforce(self) -> None:
        for i in range(1, 10):
            self.enforce_rows(i)
            self.enforce_columns(i)
            self.enforce_boxes(i)
        self.collapse()

    def as_array(self) -> np.ndarray:
        return np.array([[cell.value for cell in row] for row in self.cells])

    @property
    def is_solved(self) -> bool:
        return np.count_nonzero(self.as_array()) == 81

    @property
    def is_stuck(self) -> bool:
        stacked = np.stack([self.as_array(), self.entropy()]).sum(axis=0)
        return self.is_solved or np.count_nonzero(stacked) == 81


if __name__ == "__main__":
    easy = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    hard = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 0, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    bad = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 2, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    for puzzle in (easy, hard, bad):
        puzzle = Sudoku(puzzle)
        print(np.count_nonzero(puzzle.as_array()))
        print(puzzle.is_stuck)
        puzzle.collapse()
        puzzle.enforce()
        print(np.count_nonzero(puzzle.as_array()))
        print(puzzle.is_stuck)
        print(puzzle.as_array())
