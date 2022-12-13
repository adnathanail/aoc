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
