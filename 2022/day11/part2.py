from aocd.models import Puzzle  # type: ignore[import]

from utils import Monkey, get_operation_function, OperationType


def main() -> None:
    puzzle = Puzzle(year=2022, day=11)
    # Parse input
    product_of_divisor_tests = 1
    monkeys: dict[int, Monkey] = {}
    for monkey_data in puzzle.input_data.split("\n\n"):
        monkey_data_lines = monkey_data.split("\n")
        monkey_id = int(monkey_data_lines[0][7])
        items = [int(x) for x in monkey_data_lines[1][18:].split(", ")]
        if monkey_data_lines[2][23] == "+":
            operation = get_operation_function(OperationType.ADDITION, int(monkey_data_lines[2][25:]))
        elif monkey_data_lines[2][25:] != "old":
            operation = get_operation_function(OperationType.MULTIPLICATION, int(monkey_data_lines[2][25:]))
        else:
            operation = get_operation_function(OperationType.EXPONENTIATION, 2)

        divisble_test_number = int(monkey_data_lines[3][21:])
        product_of_divisor_tests *= divisble_test_number
        true_monkey = int(monkey_data_lines[4][29:])
        false_monkey = int(monkey_data_lines[5][30:])
        monkeys[monkey_id] = Monkey(monkey_id, items, operation, divisble_test_number, true_monkey, false_monkey)

    # Do simulation
    num_inspections = {monkey_id: 0 for monkey_id in monkeys}
    for _ in range(10000):
        for monkey in monkeys.values():
            monkey_items = monkey.items
            monkey.items = []
            for item in monkey_items:
                num_inspections[monkey.monkey_id] += 1
                new_worry_level = monkey.operation(item)
                new_worry_level = new_worry_level % product_of_divisor_tests
                if (new_worry_level % monkey.divisble_test_number) == 0:
                    monkeys[monkey.true_monkey].items.append(new_worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(new_worry_level)
    inspections_sorted = sorted(list(num_inspections.values()))
    print(inspections_sorted[-1] * inspections_sorted[-2])


if __name__ == "__main__":
    main()
