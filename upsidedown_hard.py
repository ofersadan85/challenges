from itertools import product

start = ("0", "1", "8", "00", "11", "88", "69", "96")

def upsidedown_len(l):
    if l < 3:
        return {x for x in start if len(x) == l}
    else:
        results = set()
        middle_options = upsidedown_len(l - 2)
        for middle, around in product(middle_options, start[-5:]):
            results.add(around[0] + middle + around[1])
        return results

def upsidedown(a, b):
    results = set()
    for i in range(len(a), len(b) + 1):
        results.update(upsidedown_len(i))

    results = {x for x in results if not x.startswith("0")}
    results.add("0")
    return sum(int(x) in range(int(a), int(b)) for x in results)
