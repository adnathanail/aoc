from typing import Union

from aocd.models import Puzzle  # type: ignore[import]

Packet = list[Union[int, "Packet"]]


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
    line_pairs = get_line_pairs(inp)
    return line_pairs


def parse_packet_ints(inp: str):
    pass


def parse_packet_list(inp: str, curr: int):
    if inp[curr] != "[":
        raise SyntaxError(f"Value position {curr} should be '['")
    # Move past first [
    curr += 1
    out = []
    while inp[curr] != "]":
        if inp[curr] == "[":
            new_list, curr = parse_packet_list(inp, curr)
            out.append(new_list)

        curr += 1
    return out, curr


def parse_packet(inp: str):
    return parse_packet_list(inp, 0)[0]


def main() -> None:
    puzzle = Puzzle(year=2022, day=13)
    #     pairs: list[tuple[Packet, Packet]] = parse_input("""[1,1,3,1,1]
    # [1,1,5,1,1]
    #
    # [[1],[2,3,4]]
    # [[1],4]
    #
    # [9]
    # [[8,7,6]]
    #
    # [[4,4],4,4]
    # [[4,4],4,4,4]
    #
    # [7,7,7,7]
    # [7,7,7]
    #
    # []
    # [3]
    #
    # [[[]]]
    # [[]]
    #
    # [1,[2,[3,[4,[5,6,7]]]],8,9]
    # [1,[2,[3,[4,[5,6,0]]]],8,9]""")
    #     for pair in pairs:
    #         print(pair)
    print(parse_packet("[[], [[], []]]"))
    # parse_packet("[[4,4],4,4]")


if __name__ == "__main__":
    main()
