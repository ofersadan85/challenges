import numpy as np

neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def crop_array(arr):
    arr = np.array(arr)
    while not arr[0].any():
        arr = arr[1:]
    while not arr[-1].any():
        arr = arr[:-1]
    while not arr[:, 0].any():
        arr = arr[:, 1:]
    while not arr[:, -1].any():
        arr = arr[:, :-1]
    return arr


def one_gen(cells):
    cells = np.pad(np.array(cells), (1, 1), constant_values=(0, 0))
    new_cells = np.copy(cells)
    rows, columns = cells.shape
    for y in range(rows):
        for x in range(columns):
            count_alive = 0
            for h, w in neighbors:
                if y + h in range(0, rows) and x + w in range(0, columns):
                    count_alive += cells[y + h, x + w]
            if cells[y, x]:
                new_cells[y, x] = int(count_alive in (2, 3))
            else:
                new_cells[y, x] = int(count_alive == 3)
    return new_cells.tolist()


def get_generation(cells, generations):
    for i in range(generations):
        cells = one_gen(cells)
    return crop_array(cells).tolist()
