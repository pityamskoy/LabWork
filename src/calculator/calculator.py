from LabWork.src.calculator.utility import Utility
import string as chars

"""
This class calculates any math expression, which is taken as input.
It supports only integer numbers.
"""


class Calculator:
    _operations: tuple = ("+", "-", "*", "/", "%")
    _input_string: str

    def __init__(self):
        print("Please, enter a math expression. Enter '0 0' to end the program.")
        string: str = input()

        self.set_input_string(string)
        self.execute()

    def set_input_string(self, string: str) -> None:
        if string == '0 0':
            self._input_string = string
            return

        def is_correct() -> None:
            if not self.is_input_string_correct(string):
                print("The expression contains not mathematical symbols, "
                      "including any merger of operators, or parentheses set incorrect.")
                raise ValueError

            if not self.is_math_expression_correct(string):
                print("The expression has an operator either in the end "
                      "or at the beginning, which differs from '+' and '-'.")
                raise ValueError

        flag: bool = True

        while flag:
            try:
                is_correct()

                string = self.remove_spaces(string)
                self._input_string = string
                flag = False
            except ValueError:
                print("Please, enter a correct math expression")
                string = input()

    def get_input_string(self) -> str:
        return self._input_string

    """
    Execute method is the starter of calculating, which is necessary for tracing errors.
    """

    def execute(self) -> None:
        flag = True

        while flag:
            try:
                self.calculating()
                flag = False
            except ValueError:
                print("The given math expression is incorrect.")

                string: str = input()
                self.set_input_string(string)
            except ZeroDivisionError:
                print("Entered math expression contains division by zero or "
                      "exponentiation of zero to unnatural degree.")

                string : str = input()
                self.set_input_string(string)


    """
    Calculating is the main method in the class, which splits parentheses in proper way
    and counts it. Finally, it prints a result of a math expression.

    This method works until '0 0' is given as the input string.
    """

    def calculating(self) -> None:
        string: str = self.get_input_string()

        while string != "0 0":
            while string.find("(") != -1:
                substring: str = self.parentheses_finder(string)

                if self.is_math_expression_correct(substring):
                    index: int = string.find(substring)

                    if len(string[:index]) > 2:
                        if string[index - 3: index] != "**-" and string[index - 2: index] != "**":
                            string = string[:index] + "1*" + string[index:]
                    elif len(string[:index]) > 1:
                        if string[index - 2: index] != "**":
                            string = string[:index] + "1*" + string[index:]
                    else:
                        string = "1*" + string[index:]

                    index = string.find(substring)
                    result: str = self.summation(substring[1:-1])
                    string = string[:index] + result + string[len(substring) + index:]
                else:
                    print("The given math expression is incorrect.")
                    raise ValueError

            string = self.summation(string)
            print(string)

            string = input()
            self.set_input_string(string)
            string = self.get_input_string()

    """
    Find_numbers defines left and right number from an operation and their length in the given string.
    It is necessary because the length in symbols is differ.
    For example, '2' is one symbol in a string type and '2.0' in float, what is 3 symbols.
    
    Operation_length is the exact number of symbols in an operation.
    """

    @staticmethod
    def find_numbers(string: str, operation_index: int, operation_length: int) -> tuple[
        tuple[float, int], tuple[float, int]]:
        left_number_data: tuple[float, int] = Utility.left_number_finder(
            string, Calculator._operations, operation_index)
        right_number_data: tuple[float, int] = Utility.right_number_finder(
            string, Calculator._operations, operation_index, operation_length)

        result: tuple[tuple[float, int], tuple[float, int]] = (left_number_data, right_number_data)
        return result

    """
    Parenthesis_finder finds the first pair of parenthesis, which should be executed and returns it.
    If in the argument there is no parenthesis it returns the argument.
    """

    @staticmethod
    def parentheses_finder(string: str) -> str:
        index_of_first_right_parenthesis: int = string.find(")")

        if index_of_first_right_parenthesis != -1:
            index_of_last_left_parenthesis: int = string[:index_of_first_right_parenthesis].rfind("(")
            substring: str

            if index_of_first_right_parenthesis == string[-1]:
                substring = string[index_of_last_left_parenthesis:]
            else:
                substring = string[index_of_last_left_parenthesis: index_of_first_right_parenthesis + 1]

            return substring
        else:
            return string

    """
    This method checks if a string (the most case scenario, the argument is an expression in parentheses)
    doesn't begin and doesn't end with an operator, excluding unary operator at the beginning.
    """

    @staticmethod
    def is_math_expression_correct(string: str) -> bool:
        if string[-1] in Calculator._operations:
            return False
        if string[0] not in "+-" and string[0] in Calculator._operations:
            return False
        if string in Calculator._operations:
            return False

        return True

    """
    This method checks if an input string is correct.
    """

    @staticmethod
    def is_input_string_correct(string) -> bool:
        if string.count("(") != string.count(")"):
            return False

        if string.find("()") != -1:
            return False

        last_checked_parenthesis_index: int = 0
        index_of_checking_parenthesis: int = 0

        while string[last_checked_parenthesis_index + 1:].find(")") != -1:
            index_of_checking_parenthesis += string[last_checked_parenthesis_index + 1:].find(")") + 1
            if (string[:index_of_checking_parenthesis].count("(") < string[:index_of_checking_parenthesis + 1]
                    .count(")")):
                return False
            last_checked_parenthesis_index = index_of_checking_parenthesis + 1

        list_for_checking = list(chars.ascii_letters)

        for i in chars.punctuation:
            if i not in "+-*/%().":
                list_for_checking.append(i)

        for i in chars.whitespace:
            list_for_checking.append(i)

        list_for_checking.append("***")
        list_for_checking.append("///")
        list_for_checking.append("..")

        for i in Calculator._operations:
            for j in Calculator._operations:
                list_for_checking.append(i + j)

        for i in chars.digits:
            list_for_checking.append(i + "(")
            list_for_checking.append(")" + i)

        list_for_checking.remove("**")
        list_for_checking.remove("//")
        list_for_checking.remove(" ")

        for incorrect in list_for_checking:
            if string.find(incorrect) != -1:
                return False

        return True

    """
    Remove_spaces deletes all spaces in a string if they are represented.
    """

    @staticmethod
    def remove_spaces(string: str) -> str:
        if string.find(" ") == -1:
            return string

        result: str = ""

        for i in string:
            if i != " ":
                result = result + i

        return result

    """
    This method checks if the provided string is a number.
    """

    @staticmethod
    def is_number(string: str) -> bool:
        operations = ("*", "/", "//", "%", "**")

        for operator in operations:
            if string.find(operator) != -1:
                return False

        if string.count("+") == 0 and string.count("-") == 0:
            return True

        if string.count("-") == 1 and string.count("+") == 0:
            if string[0] == "-":
                return True

        if string.count("+") == 1 and string.count("-") == 0:
            if string[0] == "+":
                return True

        return False

    """
    Practically, summation method counts the whole given math expression.
    In more details, it works like recursion. Summation calls multiplicative_operation method,
    which calls exponentiation method.
    
    The result of the summation is a number in the string type.
    """

    @staticmethod
    def summation(string: str) -> str:
        string = Calculator.multiplicative_operation(string)

        string = string.replace("--", "+")
        string = string.replace("+-", "-")
        string = string.replace("-+", "-")

        while not Calculator.is_number(string):
            result: float
            start_index: int = 0
            indexes_of_first_operations: list = list()

            if string[0] in "+-":
                start_index = 1

            index_of_first_plus: int = string[start_index:].find("+") + start_index
            index_of_first_minus: int = string[start_index:].find("-") + start_index

            if index_of_first_plus != -1:
                indexes_of_first_operations.append(index_of_first_plus)
            if index_of_first_minus != -1 and index_of_first_minus != 0:
                indexes_of_first_operations.append(index_of_first_minus)

            if len(indexes_of_first_operations) != 0:
                min_index: int = min(indexes_of_first_operations)
            else:
                break

            numbers_data: tuple[tuple[float, int], tuple[float, int]] = Calculator.find_numbers(string, min_index, 1)
            left_number: float = numbers_data[0][0]
            left_number_length: int = numbers_data[0][1]
            right_number: float = numbers_data[1][0]
            right_number_length: int = numbers_data[1][1]

            if string[0] in "+-":
                left_number = float(string[:left_number_length + 1])
                left_number_length += 1

            if index_of_first_plus == min_index:
                result = left_number + right_number
            else:
                result = left_number - right_number

            string = string[:min_index - left_number_length] + str(result) + \
                     string[min_index + right_number_length + 1:]

        string = Calculator.unary_operation(string)
        return string

    """
    Multiplicative_operations counts all operations, excluding summation and subtraction.
    The exponentiation operator is counted by calling the same named method.
    """

    @staticmethod
    def multiplicative_operation(string: str) -> str:
        string = Calculator.exponentiation(string)

        if_operator_represented_list: list = ["*" in string, "/" in string, "%" in string]

        while any(if_operator_represented_list):
            indexes_of_first_operations: list = list()
            result: float

            index_of_first_multiplication: int = string.find("*")
            index_of_first_division: int = string.find("/")
            index_of_first_int_division: int = string.find("//")
            index_of_first_remainder: int = string.find("%")
            index_of_first_multiplication_with_minus: int = string.find("*-")
            index_of_first_division_with_minus: int = string.find("/-")
            index_of_first_int_division_with_minus: int = string.find("//-")
            index_of_first_remainder_with_minus: int = string.find("%-")

            if index_of_first_multiplication != -1:
                indexes_of_first_operations.append(index_of_first_multiplication)
            if index_of_first_division != -1:
                indexes_of_first_operations.append(index_of_first_division)
            if index_of_first_int_division != -1:
                indexes_of_first_operations.append(index_of_first_int_division)
            if index_of_first_remainder != -1:
                indexes_of_first_operations.append(index_of_first_remainder)
            if index_of_first_multiplication_with_minus != -1:
                indexes_of_first_operations.append(index_of_first_multiplication_with_minus)
            if index_of_first_division_with_minus != -1:
                indexes_of_first_operations.append(index_of_first_division_with_minus)
            if index_of_first_int_division_with_minus != -1:
                indexes_of_first_operations.append(index_of_first_int_division_with_minus)
            if index_of_first_remainder_with_minus != -1:
                indexes_of_first_operations.append(index_of_first_remainder_with_minus)

            min_index: int = min(indexes_of_first_operations)

            if min_index == index_of_first_int_division:
                if string[min_index + 2] == "-":
                    numbers_data: tuple[tuple[float, int], tuple[float, int]] = Calculator.find_numbers(
                        string, min_index, 3)

                    left_number: float = numbers_data[0][0]
                    left_number_length: int = numbers_data[0][1]
                    right_number: float = numbers_data[1][0]
                    right_number_length: int = numbers_data[1][1]

                    result = float(left_number // (right_number * (-1)))
                    string = string[:min_index - left_number_length] + str(result) + \
                             string[min_index + right_number_length + 3:]
                else:
                    numbers_data: tuple[tuple[float, int], tuple[float, int]] = Calculator.find_numbers(
                        string, min_index, 2)

                    left_number: float = numbers_data[0][0]
                    left_number_length: int = numbers_data[0][1]
                    right_number: float = numbers_data[1][0]
                    right_number_length: int = numbers_data[1][1]

                    result = float(left_number // right_number)
                    string = string[:min_index - left_number_length] + str(result) + \
                             string[min_index + right_number_length + 2:]
            else:
                if string[min_index + 1] == "-":
                    numbers_data: tuple[tuple[float, int], tuple[float, int]] = Calculator.find_numbers(
                        string, min_index, 2)

                    left_number: float = numbers_data[0][0]
                    left_number_length: int = numbers_data[0][1]
                    right_number: float = numbers_data[1][0]
                    right_number_length: int = numbers_data[1][1]

                    if min_index == index_of_first_multiplication:
                        result = left_number * (right_number * (-1))
                    elif min_index == index_of_first_division:
                        result = left_number / (right_number * (-1))
                    else:
                        result = left_number % (right_number * (-1))

                    result = round(float(result), 3)
                    string = string[:min_index - left_number_length] + str(result) + \
                             string[min_index + right_number_length + 2:]

                else:
                    numbers_data: tuple[tuple[float, int], tuple[float, int]] = Calculator.find_numbers(
                        string, min_index, 1)
                    left_number: float = numbers_data[0][0]
                    left_number_length: int = numbers_data[0][1]
                    right_number: float = numbers_data[1][0]
                    right_number_length: int = numbers_data[1][1]

                    if min_index == index_of_first_multiplication:
                        result = left_number * right_number
                    elif min_index == index_of_first_division:
                        result = left_number / right_number
                    else:
                        result = left_number % right_number

                    result = round(float(result), 3)
                    string = string[:min_index - left_number_length] + str(result) + \
                             string[min_index + right_number_length + 1:]

            if_operator_represented_list = ["*" in string, "/" in string, "%" in string]
        return string

    """
    This method counts all exponentiation in a string.
    It throws ZeroDivisionError in the case of '0**0' because, by the presumption, '0**0' is prohibited.
    """

    @staticmethod
    def exponentiation(string: str) -> str:
        while string.find("**") != -1 or string.find("**-") != -1:
            index_of_first_exponentiation: int = string.find("**")
            index_of_first_exponentiation_with_minus: int = string.find("**-")
            indexes_of_first_operations: list = list()

            if index_of_first_exponentiation != -1:
                indexes_of_first_operations.append(index_of_first_exponentiation)
            if index_of_first_exponentiation_with_minus != -1:
                indexes_of_first_operations.append(index_of_first_exponentiation_with_minus)

            min_index: int = min(indexes_of_first_operations)
            result: float

            if min_index == index_of_first_exponentiation_with_minus:
                numbers_data: tuple[tuple[float, int], tuple[float, int]] = Calculator.find_numbers(
                    string, index_of_first_exponentiation, 3)

                left_number: float = numbers_data[0][0]
                left_number_length: int = numbers_data[0][1]
                right_number: float = numbers_data[1][0]
                right_number_length: int = numbers_data[1][1]

                if string[index_of_first_exponentiation - left_number_length - 1] in "+-" \
                        and string[index_of_first_exponentiation - left_number_length - 2] in "*/%+-":

                    result = round(pow(left_number * (-1), right_number * (-1)), 3)

                    string = string[:min_index - left_number_length - 1] + str(result) + \
                             string[min_index + right_number_length + 3:]
                else:
                    result = round(pow(left_number, right_number * (-1)), 3)
                    string = string[:min_index - left_number_length] + str(result) + \
                             string[min_index + right_number_length + 3:]
            else:
                numbers_data: tuple[tuple[float, int], tuple[float, int]] = (Calculator.find_numbers(
                    string, index_of_first_exponentiation, 2))

                left_number: float = numbers_data[0][0]
                left_number_length: int = numbers_data[0][1]
                right_number: float = numbers_data[1][0]
                right_number_length: int = numbers_data[1][1]

                if left_number == 0.0:
                    if not (str(right_number)[-1] == "0" and str(right_number)[-2] == ".") or right_number <= 0:
                        raise ZeroDivisionError("Exponentiation of '0' is allowed only with natural numbers.")

                if string[index_of_first_exponentiation - left_number_length - 1] in "+-" \
                        and string[index_of_first_exponentiation - left_number_length - 2] in "*/%+-":

                    result = round(pow(left_number * (-1), right_number), 3)

                    string = string[:min_index - left_number_length - 1] + str(result) + \
                             string[min_index + right_number_length + 2:]
                else:
                    result = round(pow(left_number, right_number), 3)

                    string = string[:min_index - left_number_length] + str(result) + \
                             string[min_index + right_number_length + 2:]

        return string

    """
    Unary_operation defines the sign of a number, and it regulates the sign of zero.
    Occasionally, the number '-0.0' may appear during executing the program.
    So, unary_operation fixes this problem and returns only positive zero.
    """

    @staticmethod
    def unary_operation(string: str) -> str:
        if len(string) >= 2:
            if string[0] == "-" and string[1] == "0":
                string = string[1:]
        return str(float(string))
