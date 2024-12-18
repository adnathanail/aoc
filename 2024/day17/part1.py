from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=17)
input_data = puzzle.input_data

ra_str, rb_str, rc_str, bl, prog_str = input_data.split("\n")

regs = {"A": int(ra_str[12:]), "B": int(rb_str[12:]), "C": int(rc_str[12:])}
ins = [int(x) for x in prog_str[9:].split(",")]

outs = []

ip = 0
while ip < len(ins) - 1:
    opcode, operand = ins[ip], ins[ip + 1]
    combo = opcode in [0, 2, 5, 6, 7]
    dont_inc = False
    if combo:
        if operand == 4:
            operand = regs["A"]
        elif operand == 5:
            operand = regs["B"]
        elif operand == 6:
            operand = regs["C"]
    if opcode == 0:
        regs["A"] = regs["A"] // (2**operand)
    elif opcode == 1:
        regs["B"] = operand ^ regs["B"]
    elif opcode == 2:
        regs["B"] = operand % 8
    elif opcode == 3:
        if regs["A"] != 0:
            ip = operand
            dont_inc = True
    elif opcode == 4:
        regs["B"] = regs["C"] ^ regs["B"]
    elif opcode == 5:
        outs.append(str(operand % 8))
    elif opcode == 6:
        regs["B"] = regs["A"] // (2**operand)
    elif opcode == 7:
        regs["C"] = regs["A"] // (2**operand)
    else:
        raise Exception(f"Unimplemented opcode '{opcode}'")
    if not dont_inc:
        ip += 2

print(",".join(outs))
