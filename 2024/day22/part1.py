from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=22)
input_data = puzzle.input_data


secrets = [int(x) for x in input_data.splitlines()]


def mix(a, b):
    return a ^ b


def prune(n):
    return n % 16777216


tot = 0
for secret in secrets:
    next_secret = secret
    for i in range(2000):
        next_secret = prune(mix(next_secret * 64, next_secret))
        next_secret = prune(mix(next_secret // 32, next_secret))
        next_secret = prune(mix(next_secret * 2048, next_secret))
    tot += next_secret

print(tot)
