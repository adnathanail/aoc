from typing import Union

from aocd.models import Puzzle  # type: ignore[import]

Packet = list[Union[int, "Packet"]]


def parse_packet_int(inp: str, curr: int) -> tuple[int, int]:
    out_str = ""
    while inp[curr] not in [",", "]"]:
        if inp[curr].isdigit():
            out_str += inp[curr]
            curr += 1
        else:
            raise SyntaxError(f"Value in position {curr} should be a digit")
    return int(out_str), curr


def parse_packet_list(inp: str, curr: int, depth: int) -> tuple[Packet, int]:
    if inp[curr] != "[":
        raise SyntaxError(f"Value in position {curr} should be '['")
    curr += 1

    out = []
    while curr < len(inp) and inp[curr] != "]":
        if inp[curr] == "[":
            new_list, curr = parse_packet_list(inp, curr, depth + 1)
            out.append(new_list)
        else:
            new_int, curr = parse_packet_int(inp, curr)
            out.append(new_int)
        if curr >= len(inp):
            raise SyntaxError("Input ended too soon")
        if inp[curr] == ",":
            curr += 1
        elif inp[curr] == "]":
            break
        else:
            raise SyntaxError(f"Value in position {curr} should be ',' or ']'")

    if inp[curr] != "]":
        raise SyntaxError(f"Value in position {curr} should be ']'")
    curr += 1
    return out, curr


def parse_packet(inp: str) -> Packet:
    return parse_packet_list(inp.replace(" ", ""), 0, 0)[0]


def get_line_pairs(inp: str) -> list[tuple[str, str]]:
    out = []
    lines = inp.split("\n")
    last_line = ""
    for i in range(len(lines)):
        if i % 3 == 0:
            last_line = lines[i]
        elif i % 3 == 1:
            out.append((last_line, lines[i]))
        else:
            last_line = ""
    return out


def parse_input(inp: str) -> list[tuple[Packet, Packet]]:
    return [(parse_packet(pair[0]), parse_packet(pair[1])) for pair in get_line_pairs(inp)]


def main() -> None:
    # puzzle = Puzzle(year=2022, day=13)
    pairs: list[tuple[Packet, Packet]] = parse_input("""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""")
    for pair in pairs:
        print(pair)


if __name__ == "__main__":
    main()
