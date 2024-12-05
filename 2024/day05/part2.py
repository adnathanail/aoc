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


updates_to_fix = []
for update in updates:
    if not update_follows_rules(update, rules):
        updates_to_fix.append(update)


def fix_update(u, rs):
    if len(u) == 1:
        return u
    for i in u:
        nothing_before_i = True
        for j in u:
            if i != j and (j, i) in rs:
                nothing_before_i = False
                break
        if nothing_before_i:
            return [i] + fix_update([k for k in u if k != i], rs)


tot = 0
for up in updates_to_fix:
    new_up = fix_update(up, rules)
    tot += new_up[len(new_up) // 2]
print(tot)
