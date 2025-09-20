"""
This class calculates any math expression, which is taken as input.
"""
class Calculator:
    _input_string:str
    _result:int

    def __int__(self):
        self._input_string = input("Введите выражение в калькулятор")

    def _is_such_operation_represented(self, ):
        pass

    """
    parenthesis_finder finds the first pair of parenthesis, which should be executed
    and returns it. If in the argument there is no parenthesis, returns the argument
    """
    def parenthesis_finder(self, string:str) -> str:
        index_of_first_right_parenthesis:int = string.find(')')

        if index_of_first_right_parenthesis != -1:
            index_of_last_left_parenthesis:int = string[:index_of_first_right_parenthesis].rfind('(')
            substring:str = string[index_of_last_left_parenthesis + 1:index_of_first_right_parenthesis]
            return substring
        else:
            return string

    """
    It's just a simple summator of one expression inside parenthesis
    """
    def summ_of_blocks(self, string:str) -> int:
        index_of_first_plus:int = string.find('+')
        index_of_first_minus:int = string.find('-')

        if index_of_first_plus > index_of_first_minus:
            substring:str = string[:index_of_first_plus]
        if index_of_first_plus < index_of_first_minus:
            substring:str = string[:index_of_first_minus]
        else:
            pass

    def umn(self, string:str) -> int:
        operations = tuple('*', '/', '//', '%')
        index_of_first_umn:int = string.find('*')
        index_of_first_del:int = string.find('/')
        index_of_first_pn_del:int = string.find('//')
        index_of_first_interest:int = string.find('%')

        min_index = min(index_of_first_del, index_of_first_umn, index_of_first_pn_del, index_of_first_interest)

        if min_index == -1:
            pass

        if min_index == index_of_first_del:
            substring:str = string[:index_of_first_umn]
        elif min_index == index_of_first_umn:
            substring:str = string[:index_of_first_del]
        elif min_index == index_of_first_pn_del:
            substring:str = string[:index_of_first_pn_del]
        else:
            substring:str = string[:index_of_first_interest]

    """
    pow_operation counts all exponentiation in string.
    As a result, it returns new string with counted exponentiation.
    If a string doesn't contain any '**' the method just returns this string
    """
    def pow_operation(self, string:str) -> str:
        index_of_first_pow: int = string.find('**')

        while index_of_first_pow != -1:
            operations = tuple('+', '-', '*', '/', '//', '%')

            indexes_of_operations_before_pow = list()
            indexes_of_operations_after_pow = list()
            index_of_first_operation_before_pow:int
            index_of_first_operation_after_pow:int

            index_of_next_pow:int = string[index_of_first_pow + 2:].find('*')

            # The necessary check of multiple exponentiation in a row
            if index_of_next_pow != index_of_first_pow + 2:
                for operation in operations:
                    if string[index_of_first_pow + 2:].find(operation) > index_of_first_pow + 2:
                        indexes_of_operations_after_pow.append(string[index_of_first_pow + 2:].find(operation))

                for operation in operations:
                    if string[:index_of_first_pow].rfind(operation) > -1:
                        indexes_of_operations_before_pow.append(string[:index_of_first_pow].rfind(operation))

                if len(indexes_of_operations_before_pow) > 0:
                    index_of_first_operation_before_pow = min(indexes_of_operations_before_pow)
                else:
                    index_of_first_operation_before_pow = 0

                if len(indexes_of_operations_after_pow) > 0:
                    index_of_first_operation_after_pow = min(indexes_of_operations_after_pow)
                else:
                    index_of_first_operation_after_pow = len(string)

                substring = string[index_of_first_operation_before_pow + 1:indexes_of_operations_after_pow]
                numbers = substring.split('**')
                left_number:int = int(numbers[0])
                right_number:int = int(numbers[1])
                result:int = pow(left_number, right_number)

                string = string[:index_of_first_operation_before_pow] + str(result) + string[index_of_first_operation_after_pow:]
                index_of_first_pow = string.find('**')
            else:
                index_of_last_pow_in_row:int

                while index_of_next_pow != index_of_first_pow + 2:
                    index_of_last_pow_in_row = string[index_of_next_pow:].find('**')

                    if index_of_last_pow_in_row == index_of_next_pow + 2:
                        index_of_first_pow = index_of_next_pow
                        index_of_next_pow = index_of_last_pow_in_row




        return string

    """
    unary_operation defines the sign of a number
    """
    def unary_operation(self, string:str) -> int:
        is_unary_minus: bool = '-' in string

        if is_unary_minus:
            result:int = -int(string.split('-')[-1])
        else:
            result:int = int(string[-1].split('+')[-1])

        return result