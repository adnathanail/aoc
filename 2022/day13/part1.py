from aocd.models import Puzzle  # type: ignore[import]

from utils import Packet, parse_input, packets_correctly_ordered


def main() -> None:
    puzzle = Puzzle(year=2022, day=13)
    pairs: list[tuple[Packet, Packet]] = parse_input(puzzle.input_data)
    print(sum(i + 1 for i, pair in enumerate(pairs) if packets_correctly_ordered(*pair)))


if __name__ == "__main__":
    main()
