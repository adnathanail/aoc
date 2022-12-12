from aocd.models import Puzzle  # type: ignore[import]


def main() -> None:
    puzzle = Puzzle(year=2022, day=10)
    operations = puzzle.input_data.split("\n")

    signal_strengths = []

    op_index = 0
    cycle = 0  # Initialise to 0 so loop starts nicely
    register_x = 1
    adding = False  # Set true when half-way through an adding operation
    add_value = 0  # Holds the value to be added in an adding operation
    while op_index < len(operations) or adding:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * register_x)
        # print(cycle, register_x)
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
    # print(signal_strengths)
    print(sum(signal_strengths))


if __name__ == "__main__":
    main()
