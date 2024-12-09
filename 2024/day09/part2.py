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
    while (end_ptr + 1) < len(disk) and disk[end_ptr + 1] == disk[start_ptr]:
        end_ptr += 1
    return end_ptr


def find_free_space(disk, length):
    free_ptr = disk.index(".")
    while free_ptr < len(disk):
        if disk[free_ptr] == ".":
            free_ptr_end = get_block_end(disk, free_ptr)
            free_space_length = free_ptr_end - free_ptr + 1
            if free_space_length >= length:
                return free_ptr
            free_ptr = free_ptr_end + 1
        free_ptr += 1
    return None


def do_shunt(disk, block_id):
    block_start = disk.index(chr(block_id))
    block_end = get_block_end(disk, block_start)
    block_length = block_end - block_start + 1

    free_space_ptr = find_free_space(disk, block_length)
    if free_space_ptr is None:
        return False

    if free_space_ptr < block_start:
        for x in range(block_length):
            disk[free_space_ptr + x] = chr(block_id)
            disk[block_start + x] = "."

    return True


def shunt_disk(disk):
    shunted = disk.copy()
    free_ptr = shunted.index(".")
    block_ids_decreasing = sorted(set([ord(char) for char in shunted[free_ptr:]]))[::-1]
    for bi in block_ids_decreasing:
        do_shunt(shunted, bi)
    return shunted


def score_disk(shunted):
    score = 0
    for i in range(len(shunted)):
        if shunted[i] == ".":
            continue
        score += i * (ord(shunted[i]) - 100)
    return score


print(score_disk(shunt_disk(expand_disk(input_data))))
