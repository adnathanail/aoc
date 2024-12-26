from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=24)
input_data = puzzle.input_data
wires_to_swap = [
    ("hmk", "z16"),
    ("fhp", "z20"),
    ("rvf", "tpc"),
    ("fcd", "z33"),
]
for w1, w2 in wires_to_swap:
    input_data = input_data.replace(f"-> {w1}", "-> 🦀")
    input_data = input_data.replace(f"-> {w2}", f"-> {w1}")
    input_data = input_data.replace("-> 🦀", f"-> {w2}")

starts_str, gates_str = input_data.split("\n\n")

initial_wires = {}
for start_str in starts_str.split("\n"):
    wire, value_str = start_str.split(": ")
    if value_str == "0":
        initial_wires[wire] = False
    elif value_str == "1":
        initial_wires[wire] = True
    else:
        raise Exception(f"Invalid wire '{value_str}")


gates = []
for gate_str in gates_str.split("\n"):
    in1, op, in2, _, outt = gate_str.split(" ")
    gates.append((in1, in2, op, outt))


def wires_to_dec(wires, prefix):
    wire_names = sorted([wire for wire in wires if wire[0] == prefix])[::-1]
    # for w1, w2 in wires_to_swap:
    #     wind1, wind2 = wire_names.index(w1), wire_names.index(w2)
    #     wire_names[wind1], wire_names[wind2] = wire_names[wind2], wire_names[wind1]
    wire_values = ["1" if wires[w] else "0" for w in wire_names]
    return int("".join(wire_values), 2)

def run_circuit(wires):
    gates_to_proc = gates.copy()
    while gates_to_proc:
        gates_to_remove = []
        for i in range(len(gates_to_proc)):
            gate = gates_to_proc[i]
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
            gates_to_proc.pop(j)

    return wires_to_dec(wires, "z")

def dec_to_wires(x, y):
    out = {w: False for w in initial_wires}
    x_bits = bin(x)[2:][::-1]
    for i in range(len(x_bits)):
        out[f"x{i:02}"] = x_bits[i] == "1"
    y_bits = bin(y)[2:][::-1]
    for i in range(len(y_bits)):
        out[f"y{i:02}"] = y_bits[i] == "1"
    return out


br = False
for l in range(1, 44):
    for m in range(1, 44):
        f, g = (2 ** l) - 1, (2**m) - 1
        wi = dec_to_wires(f, g)
        out = run_circuit(wi)
        if f + g != out:
            print("BAD")
            print(bin(f), len(bin(f)) - 2)
            print(bin(g), len(bin(g)) - 2)
            print(out)
            br = True
            break
    if br:
        break

print(",".join(sorted([wire for pair in wires_to_swap for wire in pair])))