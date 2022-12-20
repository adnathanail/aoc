from functools import cmp_to_key
from typing import Literal

from aocd.models import Puzzle  # type: ignore[import]

from utils import Packet, parse_input, packets_correctly_ordered


def packet_cmp(left_packet: Packet, right_packet: Packet) -> Literal[-1, 0, 1]:
    match packets_correctly_ordered(left_packet, right_packet):
        case True:
            return -1
        case False:
            return 1
        case _:
            return 0


def main() -> None:
    puzzle = Puzzle(year=2022, day=13)
    pairs: list[tuple[Packet, Packet]] = parse_input(puzzle.input_data)
    # Flatten [(Packet, Packet), ...] to [Packet, Packet, ...]
    flattened_pairs = [item for sublist in pairs for item in sublist]
    # Add divider packets
    flattened_pairs.extend(([[2]], [[6]]))
    # Sort packets
    sorted_packets = sorted(flattened_pairs, key=cmp_to_key(packet_cmp))
    # Calculate decoder key
    print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))


if __name__ == "__main__":
    main()
