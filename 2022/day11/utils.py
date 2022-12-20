from enum import Enum
from typing import Callable


class Monkey:
    def __init__(
        self,
        monkey_id: int,
        items: list[int],
        operation: Callable[[int], int],
        divisble_test_number: int,
        true_monkey: int,
        false_monkey: int,
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


def get_operation_function(
    op_type: OperationType, op_input: int
) -> Callable[[int], int]:
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
                return x**op_input

            return exp


def parse_monkey_data(inp: str) -> tuple[dict[int, Monkey], int]:
    monkeys = {}
    product_of_divisor_tests = 1
    for monkey_data in inp.split("\n\n"):
        monkey_data_lines = monkey_data.split("\n")
        monkey_id = int(monkey_data_lines[0][7])
        items = [int(x) for x in monkey_data_lines[1][18:].split(", ")]
        if monkey_data_lines[2][23] == "+":
            operation = get_operation_function(
                OperationType.ADDITION, int(monkey_data_lines[2][25:])
            )
        elif monkey_data_lines[2][25:] != "old":
            operation = get_operation_function(
                OperationType.MULTIPLICATION, int(monkey_data_lines[2][25:])
            )
        else:
            operation = get_operation_function(OperationType.EXPONENTIATION, 2)

        divisble_test_number = int(monkey_data_lines[3][21:])
        product_of_divisor_tests *= divisble_test_number
        true_monkey = int(monkey_data_lines[4][29:])
        false_monkey = int(monkey_data_lines[5][30:])
        monkeys[monkey_id] = Monkey(
            monkey_id, items, operation, divisble_test_number, true_monkey, false_monkey
        )
    return monkeys, product_of_divisor_tests
