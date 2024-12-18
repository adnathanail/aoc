from aocd.models import Puzzle


# Decompiler
puzzle = Puzzle(year=2024, day=17)
input_data = puzzle.input_data

ra_str, rb_str, rc_str, bl, prog_str = input_data.split("\n")

regs = {"A": int(ra_str[12:]), "B": int(rb_str[12:]), "C": int(rc_str[12:])}
ins = [int(x) for x in prog_str[9:].split(",")]

for ip in range(0, len(ins), 2):
    opcode, operand = ins[ip], ins[ip + 1]
    combo = opcode in [0, 2, 5, 6, 7]
    dont_inc = False
    if combo:
        if operand == 4:
            operand = "A"
        elif operand == 5:
            operand = "B"
        elif operand == 6:
            operand = "C"
    if opcode == 0:
        print(f"A = A // (2**{operand})")
    elif opcode == 1:
        print(f"B = {operand} ^ B")
    elif opcode == 2:
        print(f"B = {operand} % 8")
    elif opcode == 3:
        print(f"Jump to {operand} if A != 0")
    elif opcode == 4:
        print(f"B = C ^ B")
    elif opcode == 5:
        print(f"Out {operand} % 8")
    elif opcode == 6:
        print(f"B = A // (2**{operand})")
    elif opcode == 7:
        print(f"C = A // (2**{operand})")
    else:
        raise Exception(f"Unimplemented opcode '{opcode}'")


# Hand-written optimised version of my specific input
def run_prog(A):
    B = 0
    C = 0

    out = []

    while A != 0:
        B = (A % 8) ^ 1
        C = A // (2**B)
        B = 5 ^ B ^ C
        out.append(B % 8)
        A = A // (2**3)

    return out


# Test original program is still outputting correctly
print(run_prog(64854237) == [4, 1, 7, 6, 4, 1, 0, 2, 7])


# Implement in rust
# - Inline 2**3
# - Replace // (2**X) with >> X
# - Move a assignment to the start of the loop so that the last thing can be adding to the list
# - Inline C register calculation
# - Replace reg_a = reg_a >> 3 with reg_a >>= 3 seems to remove about 5-10ms on 10,000,000 iterations
# - Replacing % 8 with & 0b111 removes 20-40 ms on 10,000,000 iterations
# - Inlining the reg_b = (reg_a & bit_mask) ^ 1 into the next reg_b assignment saves about 30ms, even though it means duplicating calculations!
# - This allowed creating reg_b as a fresh variable each loop instead of having a single mutable vec, taking off another 10ms
# - Adding #[inline(always)] removed a further 30ms
# - Enabling optimised compiling (-O) knocked off about 150ms!
# - Return early from program if the first number returned isn't right
# - Only allocate 1 array, and give it to each program run
# - Return a bool from the program, as opposed to the result array (reduces memory messes)


# Manual search, digit by digit, starting from the right
#   in general numbers were independent, but if there were multiple options for a given position, some worked and some didn't
#   this only seemed to affect the next number in sequence, which made it easy to roll-back by hand without needing proper recursion
def octal_digits_to_dec(digs):
    tot = 0
    for i in range(len(digs)):
        # print(i, digs[i], (8**i) * digs[i])
        tot += (8**i) * digs[i]
    return tot


for j in range(8):
    print(j, run_prog(octal_digits_to_dec([j, 5, 7, 2, 7, 6, 2, 3, 7, 0, 6, 4, 4, 6, 2, 5, 4])))

print(octal_digits_to_dec([5, 7, 2, 7, 6, 2, 3, 7, 0, 6, 4, 4, 6, 2, 5, 4]))
print(run_prog(164279024971453))
