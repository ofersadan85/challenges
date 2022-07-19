invalid = "23457"
valid_pairs = ("00", "11", "88", "69", "96")


def split(s):
    l = len(s)
    a, b = s[: l // 2 + 1], s[::-1][: l // 2 + 1]
    return a, b


def is_valid(n):
    n = str(n)
    for c in invalid:
        if c in n:
            return False

    for a, b in zip(*split(n)):
        if a + b not in valid_pairs:
            return False

    return True


def upsidedown(a, b):
    return sum(is_valid(n) for n in range(int(a), int(b)))


if __name__ == "__main__":
    for i in range(0, 10000):
        if is_valid(i):
            print(i)
