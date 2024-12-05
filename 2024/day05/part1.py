from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=5)
input_data = puzzle.input_data

rules_str, updates_str = input_data.split("\n\n")

rules = []
for row in rules_str.split("\n"):
    a, b = row.split("|")
    rules.append((int(a), int(b)))

updates = []
for row in updates_str.split("\n"):
    updates.append([int(x) for x in row.split(",")])


def update_follows_rules(u, rs):
    for r in rs:
        if r[0] in u and r[1] in u:
            if u.index(r[0]) > u.index(r[1]):
                return False
    return True


tot = 0
for update in updates:
    if update_follows_rules(update, rules):
        tot += update[len(update) // 2]

print(tot)
