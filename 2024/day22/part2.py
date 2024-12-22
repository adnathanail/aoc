from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=22)
input_data = puzzle.input_data

secrets = [int(x) for x in input_data.splitlines()]


def mix(a, b):
    return a ^ b


def prune(n):
    return n % 16777216


def get_next_secret(prev_secret):
    a = prune(mix(prev_secret * 64, prev_secret))
    b = prune(mix(a // 32, a))
    return prune(mix(b * 2048, b))


c2p_list = []
for secret in secrets:
    prev_price = secret % 10
    prices = [prev_price]
    changes = []
    for i in range(2000):
        secret = get_next_secret(secret)
        price = secret % 10
        prices.append(price)
        changes.append(price - prev_price)
        prev_price = price
    changes_to_price = {}
    for j in range(4, len(prices)):
        if tuple(changes[j - 4 : j]) not in changes_to_price:
            changes_to_price[tuple(changes[j - 4 : j])] = prices[j]
    c2p_list.append(changes_to_price)

c_to_try = set()
for c2p in c2p_list:
    for item in c2p.keys():
        c_to_try.add(item)


best_tot = 0
for c in c_to_try:
    tot = 0
    for c2p in c2p_list:
        if c in c2p:
            tot += c2p[c]

    best_tot = max(tot, best_tot)


print(best_tot)
