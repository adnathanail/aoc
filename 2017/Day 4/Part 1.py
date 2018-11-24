from aocd import get_data
inp = get_data(day=4)

count = 0
for p in inp.split('\n'):
    used_words = []
    valid = True
    for word in p.split(" "):
        if word in used_words:
            valid = False
            continue
        used_words.append(word)
    if valid:
        count += 1
print(count)
