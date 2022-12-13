from aocd.models import Puzzle  # type: ignore[import]

from utils import parse_monkey_data


def main() -> None:
    puzzle = Puzzle(year=2022, day=11)

    monkeys, product_of_divisor_tests = parse_monkey_data(puzzle.input_data)
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
