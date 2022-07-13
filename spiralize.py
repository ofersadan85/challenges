import numpy as np

def spiralize(size):
    if size == 1:
        return [[1]]
    spiral = np.ones((size, size), dtype=int)
    spiral[1:-1, 1:-1] = 0
    spiral[1, 0] = 0
    if size > 4:
        spiral[2, 1] = 1
        spiral[2:-2, 2:-2] = spiralize(spiral.shape[0] - 4)
    return spiral

if __name__ == '__main__':
    for i in range(1, 20):
        print(i)
        print(spiralize(i))
