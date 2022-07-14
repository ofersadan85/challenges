import numpy as np


def cell_options(sudoku: np.ndarray, x: int, y: int) -> set:
    options = set(range(1, 10))
    options -= set(sudoku[x, :])
    options -= set(sudoku[:, y])
    x0 = x // 3 * 3
    y0 = y // 3 * 3
    options -= set(sudoku[x0 : x0 + 3, y0 : y0 + 3].flatten())
    return options


def brute_force(sudoku: np.ndarray) -> np.ndarray:
    change = True
    while change:
        change = False
        for x, y in zip(*np.where(sudoku == 0)):
            result = cell_options(sudoku, x, y)
            if len(result) == 1:
                sudoku[x, y] = result.pop()
                change = True
    return sudoku


if __name__ == "__main__":
    puzzle = [
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
    print(np.count_nonzero(puzzle))
    puzzle = np.array(puzzle, dtype=int)
    puzzle = brute_force(puzzle)
    print(puzzle)
    print(np.count_nonzero(puzzle))
