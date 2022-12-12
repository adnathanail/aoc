from aocd.models import Puzzle  # type: ignore[import]


def main() -> None:
    puzzle = Puzzle(year=2022, day=10)
    operations = puzzle.input_data.split("\n")

    op_index = 0
    cycle = 0  # Initialise to 0 so loop starts nicely
    register_x = 1
    adding = False  # Set true when half-way through an adding operation
    add_value = 0  # Holds the value to be added in an adding operation
    while op_index < len(operations) or adding:
        cycle += 1
        if register_x in [(cycle % 40) - 2, (cycle % 40) - 1, (cycle % 40)]:
            print("#", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            # print()
            print()
        if not adding:
            op = operations[op_index]
            op_index += 1
            match op[:4]:
                case "noop":
                    pass
                case "addx":
                    adding = True
                    add_value = int(op.split(" ")[1])
                case _:
                    raise Exception("panic!")
        else:
            register_x += add_value
            adding = False
    # It prints FGCUZREC


if __name__ == "__main__":
    main()
