# write your code here
class Calculator:
    def __init__(self):
        self.operands = []
        self.operator = []
        self.original = ""
        self.variables = {}

    def process_variables(self, input_: str):
        """
        Process input and get variable
        Args:
            input_:

        Returns:
            -1 error
            0 ok
        """
        variables = input_.strip().split("=")
        variables = [variable.strip() for variable in variables]  # remove space
        if len(variables) < 1:  # error
            return -1
        elif len(variables) == 1:  # if just one variable just print
            if not input_.isalpha():
                print('Invalid assignment')
                return -1
            else:
                try:
                    print(int(self.variables[variables[0]]))
                    return 0
                except KeyError:
                    print("Unknown variable")
                    return -1
        elif len(variables) >= 2:  # assigment form right to left
            if not variables[0].isalpha():  # the example just check the first one
                print('Invalid identifier')
                return -1
            variables.reverse()
            for i in range(len(variables) - 1):  # check something like a=8=9
                if variables[i].isdigit() and variables[i + 1].isdigit():
                    print('Invalid assignment')
                    return -1
            for i in range(len(variables) - 1):
                if variables[i].isdigit():
                    self.variables[variables[i + 1]] = float(variables[i])
                elif variables[i].isalpha():
                    try:
                        self.variables[variables[i + 1]] = self.variables[variables[i]]
                    except KeyError:
                        print('Unknown variable')
                        return -1
                else:
                    print('Invalid assignment')
                    return -1
        else:
            pass
        return 0

    def process_operands_operators(self, user_input: str) -> None:
        """
        analysis input. try to get operands and operators, and can process +++ or ---
        Args:
            user_input:
        todo: try to make a split func by '+ - * /', not split by " "
        """
        self.original = user_input
        self.operator = []
        self.operands = []
        user_input = user_input.split()
        for val in user_input:
            if val.isdigit():  # process number
                self.operands.append(int(val))
            else:
                if val.isalpha():  # process variable
                    try:
                        self.operands.append(self.variables[val])  # get variable value
                        continue
                    except KeyError:
                        print('Unknown variable')
                        break
                if val.startswith('-') and val.replace('-', "").isdigit():  # process neg number
                    self.operands.append(int(val))
                    continue
                if val.startswith('+') and val.replace('+', "").isdigit():  # process neg number
                    self.operands.append(int(val))
                    continue
                count_min = val.count('-')
                if count_min % 2 == 0:
                    self.operator.append('+')
                else:
                    self.operator.append('-')
        if len(self.operator) != (len(self.operands) - 1):
            raise Exception("Operator Error")  # raise ERROR

    def get_result(self):
        """
        calculate by operands and operators
        Returns:

        """
        result = self.operands[0]
        i = 0
        if len(self.operands) == 1 or len(self.operator) == 0:  # just one number
            return self.operands[0]
        for val in self.operands[1:]:
            if self.operator[i] == '+':
                result += val
            elif self.operator[i] == '-':
                result -= val
            i += 1
        return int(result)  # result need to be int

    def run(self):
        while True:
            input_ = input()
            if "/" in input_:
                if input_ == "/exit":
                    print("Bye!")
                    break
                else:
                    print("Unknown command")
            elif "=" in input_:
                self.process_variables(input_)
            elif '+' in input_ or '-' in input_ or '*' in input_ or '/' in input_:
                try:
                    self.process_operands_operators(input_)
                    print(self.get_result())
                except Exception:
                    print("Invalid expression")
            else:
                if input_ == "":
                    pass
                elif len(input_.split()) == 1:
                    self.process_variables(input_)


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.run()