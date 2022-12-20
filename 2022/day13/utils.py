from typing import Optional, Union

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


def packets_correctly_ordered(left_packet: Packet, right_packet: Packet) -> Optional[bool]:
    for i in range(min(len(left_packet), len(right_packet))):
        left_val = left_packet[i]
        right_val = right_packet[i]
        if type(left_val) == int and type(right_val) == list:
            left_val = [left_val]
        elif type(left_val) == list and type(right_val) == int:
            right_val = [right_val]

        if type(left_val) == int and type(right_val) == int:
            if left_val < right_val:
                return True
            elif left_val > right_val:
                return False
            else:
                continue
        elif type(left_val) == list and type(right_val) == list:
            cmp_result = packets_correctly_ordered(left_val, right_val)
            if cmp_result is True:
                return True
            elif cmp_result is False:
                return False
            else:
                continue
    # If all input up to the common length of the two inputs was comparably the same, check lengths of packet
    if len(left_packet) != len(right_packet):
        return len(left_packet) < len(right_packet)
