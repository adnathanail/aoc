from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=15)


def HASH(st):
    curr = 0
    for char in st:
        curr += ord(char)
        curr *= 17
        curr %= 256

    return curr


boxes = {i: list() for i in range(256)}

for step in puzzle.input_data.split(","):
    if "=" in step:
        label, lens = step.split("=")
        box = HASH(label)
        replaced = False
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                boxes[box][i] = (label, int(lens))
                replaced = True
                break
        if not replaced:
            boxes[box].append((label, int(lens)))
    elif "-" in step:
        label = step.split("-")[0]
        box = HASH(label)
        for i in range(len(boxes[box])):
            if boxes[box][i][0] == label:
                del boxes[box][i]
                break
    else:
        raise Exception


tot = 0

for box in boxes:
    if len(boxes[box]) > 0:
        for i, lens in enumerate(boxes[box]):
            tot += (box + 1) * (i + 1) * lens[1]

print(tot)
