from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=24)
input_data = puzzle.input_data
starts_str, gates_str = input_data.split("\n\n")

wires = {}
for start_str in starts_str.split("\n"):
    wire, value_str = start_str.split(": ")
    if value_str == "0":
        wires[wire] = False
    elif value_str == "1":
        wires[wire] = True
    else:
        raise Exception(f"Invalid wire '{value_str}")

gates = []
for gate_str in gates_str.split("\n"):
    in1, op, in2, _, outt = gate_str.split(" ")
    gates.append((in1, in2, op, outt))


while gates:
    gates_to_remove = []
    for i in range(len(gates)):
        gate = gates[i]
        if gate[0] in wires and gate[1] in wires:
            if gate[2] == "AND":
                result = wires[gate[0]] and wires[gate[1]]
            elif gate[2] == "OR":
                result = wires[gate[0]] or wires[gate[1]]
            elif gate[2] == "XOR":
                result = wires[gate[0]] != wires[gate[1]]
            else:
                raise Exception(f"Invalid gate '{gate[2]}'")
            wires[gate[3]] = result
            gates_to_remove.append(i)
    for j in gates_to_remove[::-1]:
        gates.pop(j)


z_wire_names = sorted([wire for wire in wires if wire[0] == "z"])[::-1]
z_wire_values = ["1" if wires[w] else "0" for w in z_wire_names]
print(int("".join(z_wire_values), 2))
