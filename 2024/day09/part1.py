from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=9)
input_data = puzzle.input_data


def expand_disk(dense):
    dense += "0"

    disk = ""
    block_id = 0
    for i in range(0, len(dense), 2):
        disk += chr(block_id + 100) * int(dense[i])
        disk += "." * int(dense[i + 1])
        block_id += 1

    return list(disk)


def get_block_end(disk, start_ptr):
    end_ptr = start_ptr
    while disk[end_ptr] == disk[start_ptr] and end_ptr < (len(disk) - 1):
        end_ptr += 1
    return end_ptr


def do_shunt(disk):
    free_ptr = disk.index(".")
    free_end_ptr = get_block_end(disk, free_ptr)
    free_block_length = free_end_ptr - free_ptr

    i = free_ptr
    while i < len(disk):
        if disk[i] != ".":
            be = get_block_end(disk, i)
            print(disk[i], i, be, be - i)
            i = be + 1
        else:
            i += 1


def shunt_disk(disk):
    shunted = disk.copy()
    free_ptr = -1
    end_ptr = len(disk)
    while True:
        end_ptr -= 1
        while shunted[end_ptr] == ".":
            end_ptr -= 1
        free_ptr += 1
        while shunted[free_ptr] != ".":
            free_ptr += 1
        if end_ptr < free_ptr:
            return shunted
        shunted[free_ptr] = shunted[end_ptr]
        shunted[end_ptr] = "."


def score_disk(shunted):
    score = 0
    for i in range(len(shunted)):
        if shunted[i] == ".":
            break
        score += i * (ord(shunted[i]) - 100)
    return score


print(score_disk(shunt_disk(expand_disk(input_data))))
