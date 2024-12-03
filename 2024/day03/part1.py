from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=3)
input_data = puzzle.input_data


def lex(inp):
    i = 0
    tokens = []
    while i < len(inp):
        if inp[i] == "m":
            old_i = i
            i, found = lex_m(inp, i + 1)
            if found:
                tokens.append(inp[old_i:i])
        else:
            i += 1
    return tokens


def lex_m(inp, i):
    if inp[i] == "u":
        return lex_mu(inp, i + 1)
    else:
        return i + 1, False


def lex_mu(inp, i):
    if inp[i] == "l":
        return lex_mul(inp, i + 1)
    else:
        return i + 1, False


def lex_mul(inp, i):
    if inp[i] == "(":
        return lex_mul_br(inp, i + 1)
    else:
        return i + 1, False


def lex_mul_br(inp, i):
    if inp[i].isnumeric():
        return lex_mul_br(inp, i + 1)
    elif inp[i] == ",":
        return lex_mul_br_num_comma(inp, i + 1)
    else:
        return i + 1, False


def lex_mul_br_num_comma(inp, i):
    if inp[i].isnumeric():
        return lex_mul_br_num_comma(inp, i + 1)
    elif inp[i] == ")":
        return i + 1, True
    else:
        return i + 1, False


def parse(toks):
    tot = 0
    for tok in toks:
        a, b = tok[4:-1].split(",")
        tot += int(a) * int(b)
    return tot


print(parse(lex(input_data)))
