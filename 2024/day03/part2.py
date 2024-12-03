from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=3)
input_data = puzzle.input_data


def lex(inp):
    i = 0
    tokens = []
    while i < len(inp):
        old_i = i
        if inp[i] == "m":
            i, found = lex_m(inp, i + 1)
            if found:
                tokens.append(inp[old_i:i])
        elif inp[i] == "d":
            i, found = lex_d(inp, i + 1)
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


def lex_d(inp, i):
    if inp[i] == "o":
        return lex_do(inp, i + 1)
    else:
        return i + 1, False


def lex_do(inp, i):
    if inp[i] == "(":
        return lex_do_br(inp, i + 1)
    elif inp[i] == "n":
        return lex_don(inp, i + 1)
    else:
        return i + 1, False


def lex_do_br(inp, i):
    if inp[i] == ")":
        return i + 1, True
    else:
        return i + 1, False


def lex_don(inp, i):
    if inp[i] == "'":
        return lex_don_ap(inp, i + 1)
    else:
        return i + 1, False


def lex_don_ap(inp, i):
    if inp[i] == "t":
        return lex_don_ap_t(inp, i + 1)
    else:
        return i + 1, False


def lex_don_ap_t(inp, i):
    if inp[i] == "(":
        return lex_don_ap_t_br(inp, i + 1)
    else:
        return i + 1, False


def lex_don_ap_t_br(inp, i):
    if inp[i] == ")":
        return i + 1, True
    else:
        return i + 1, False


def parse(toks):
    tot = 0
    enabled = True
    for tok in toks:
        if tok == "do()":
            enabled = True
        elif tok == "don't()":
            enabled = False
        elif enabled:
            a, b = tok[4:-1].split(",")
            tot += int(a) * int(b)
    return tot


print(parse(lex(input_data)))
