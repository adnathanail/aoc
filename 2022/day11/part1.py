from enum import Enum
from typing import Callable

from aocd.models import Puzzle  # type: ignore[import]


class Monkey:
    def __init__(
            self,
            monkey_id: int,
            items: list[int],
            operation: Callable[[int], int],
            divisble_test_number: int,
            true_monkey: int,
            false_monkey: int
    ):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.divisble_test_number = divisble_test_number
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def __str__(self):
        return f"{self.monkey_id} - {self.items}"


class OperationType(Enum):
    ADDITION = "addition"
    MULTIPLICATION = "multiplication"
    EXPONENTIATION = "exponentiation"


def get_operation_function(op_type: OperationType, op_input: int) -> Callable[[int], int]:
    match op_type:
        case OperationType.ADDITION:
            def add(x):
                return x + op_input

            return add
        case OperationType.MULTIPLICATION:
            def mult(x):
                return x * op_input

            return mult
        case OperationType.EXPONENTIATION:
            def exp(x):
                return x ** op_input

            return exp


def main() -> None:
    puzzle = Puzzle(year=2022, day=11)
    # Parse input
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
        true_monkey = int(monkey_data_lines[4][29:])
        false_monkey = int(monkey_data_lines[5][30:])
        monkeys[monkey_id] = Monkey(monkey_id, items, operation, divisble_test_number, true_monkey, false_monkey)

    # Do simulation
    num_inspections = {monkey_id: 0 for monkey_id in monkeys}
    for _ in range(20):
        for monkey in monkeys.values():
            monkey_items = monkey.items
            monkey.items = []
            for item in monkey_items:
                num_inspections[monkey.monkey_id] += 1
                new_worry_level = monkey.operation(item)
                new_worry_level = new_worry_level // 3
                if (new_worry_level % monkey.divisble_test_number) == 0:
                    monkeys[monkey.true_monkey].items.append(new_worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(new_worry_level)
    inspections_sorted = sorted(list(num_inspections.values()))
    print(inspections_sorted[-1] * inspections_sorted[-2])


if __name__ == "__main__":
    main()
