from aocd.models import Puzzle

# puzzle = Puzzle(year=2024, day=17)
# input_data = puzzle.input_data

# ra_str, rb_str, rc_str, bl, prog_str = input_data.split("\n")

# regs = {"A": int(ra_str[12:]), "B": int(rb_str[12:]), "C": int(rc_str[12:])}
# ins = [int(x) for x in prog_str[9:].split(",")]

# for ip in range(0, len(ins), 2):
#     opcode, operand = ins[ip], ins[ip + 1]
#     combo = opcode in [0, 2, 5, 6, 7]
#     dont_inc = False
#     if combo:
#         if operand == 4:
#             operand = "A"
#         elif operand == 5:
#             operand = "B"
#         elif operand == 6:
#             operand = "C"
#     if opcode == 0:
#         print(f"A = A // (2**{operand})")
#     elif opcode == 1:
#         print(f"B = {operand} ^ B")
#     elif opcode == 2:
#         print(f"B = {operand} % 8")
#     elif opcode == 3:
#         print(f"Jump to {operand} if A != 0")
#     elif opcode == 4:
#         print(f"B = C ^ B")
#     elif opcode == 5:
#         print(f"Out {operand} % 8")
#     elif opcode == 6:
#         print(f"B = A // (2**{operand})")
#     elif opcode == 7:
#         print(f"C = A // (2**{operand})")
#     else:
#         raise Exception(f"Unimplemented opcode '{opcode}'")


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

print(run_prog(64854237) == [4,1,7,6,4,1,0,2,7])

for i in range(10000000):
    if i % 1000 == 0:
        print(i)
    assert run_prog(i) != [4,1,7,6,4,1,0,2,7]