"""
This is the utility class for Calculator.
"""


class Utility:
    """
    Left_number_finder defines left number from an operation and number's length in the given string.
    """

    @staticmethod
    def left_number_finder(string: str, operations: tuple, index_of_last_operation: int) -> tuple[float, int]:
        indexes_of_first_operations: list = list()
        number: float
        length_of_number: int

        for operation in operations:
            indexes_of_first_operations.append(string[:index_of_last_operation].rfind(operation))

        index_of_first_operation: int = max(indexes_of_first_operations)
        if index_of_first_operation != -1:
            number = float(string[index_of_first_operation + 1: index_of_last_operation])
            length_of_number = len(string[index_of_first_operation + 1: index_of_last_operation])
        else:
            number = float(string[:index_of_last_operation])
            length_of_number = len(string[:index_of_last_operation])

        if number == -0.0:
            number = 0.0

        number = round(number, 5)

        result: tuple[float, int] = (number, length_of_number)
        return result

    """
    Right_number_finder defines right number from an operation and number's length in the given string.
    """

    @staticmethod
    def right_number_finder(string: str, operations: tuple, operation_index: int, operation_length: int) -> tuple[
        float, int]:
        indexes_of_first_operations = list()
        number: float
        length_of_number: int

        for operation in operations:
            if string[operation_index + operation_length:].find(operation) != -1:
                indexes_of_first_operations.append(string[operation_index + operation_length:].find(operation))

        if len(indexes_of_first_operations) != 0:
            index_of_first_operation: int = min(indexes_of_first_operations)
            if index_of_first_operation != -1:
                number = float(string[operation_index + operation_length:
                                      operation_index + index_of_first_operation + operation_length])
                length_of_number = len(string[operation_index + operation_length:
                                              operation_index + index_of_first_operation + operation_length])
            else:
                number = float(string[operation_index + operation_length:])
                length_of_number = len(string[operation_index + operation_length:])
        else:
            number = float(string[operation_index + operation_length:])
            length_of_number = len(string[operation_index + operation_length:])

        if number == -0.0:
            number = 0.0

        result: tuple[float, int] = (number, length_of_number)
        return result
