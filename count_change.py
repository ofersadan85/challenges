def count_change(money, coins):
    options = []
    for i, coin in enumerate(coins):
        if coin == money:
            options.append([coin])
        elif coin < money:
            options += [[coin] + x for x in count_change(money - coin, coins[i:])]
    return options


if __name__ == "__main__":
    print(count_change(4, [1, 2]))
    print(count_change(10, [5, 2, 3]))
    print(count_change(11, [5, 7]))
    print(count_change(10, [5, 2, 3]))
    # print(count_change(100, [1, 5, 10, 25, 50]))
