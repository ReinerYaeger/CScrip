
class Interpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, parse_tree):
        if parse_tree is None:
            return None

        input_entry = parse_tree[0]

        if input_entry == 'program_start':
            self.execute = (parse_tree[1])
        elif input_entry == 'data_structure':
            self.execute = (parse_tree[1])
        elif input_entry == 'list_structure':
            self.execute = (parse_tree[1])
        elif input_entry == 'empty':
            self.execute = (parse_tree[2])
        elif input_entry == 'program':
            if len(parse_tree) <= 6:
                self.execute = (parse_tree[1][2][3][4][5])
            else:
                self.execute = (parse_tree[1][2][3][4][5][6][7][8][9])
        elif input_entry == 'type_declaration':
            self.execute = (parse_tree[1])
        elif input_entry == 'statement':
            self.execute == (parse_tree[1])
        elif input_entry == 'conditional_statement':
            if len(parse_tree) == 1:
                self.execute = (parse_tree[1])
            elif len(parse_tree) == 2:
                self.execute = (parse_tree[1][2])
            elif len(parse_tree) == 3:
                self.execute = (parse_tree[1][2][3])
            elif len(parse_tree) > 8:
                self.execute = (parse_tree[1][2][4][5][6])
        elif input_entry == 'if_block':
            self.execute = (parse_tree[1][2][4])
        elif input_entry == 'else_block':
            self.execute = (parse_tree[1][2][4])
        elif input_entry == 'elif_block':
            self.execute = (parse_tree[1][2][3][5])
        elif input_entry == 'inequalities':
            if len(parse_tree) <= 4:
                self.execute = (parse_tree[2][1][3])
        elif input_entry == 'inequalities_sym':
            self.execute = (parse_tree[1])
        elif input_entry == 'function_parameter':
            if len(parse_tree) == 2:
                self.execute = (parse_tree[1])
            else:
                self.execute = (parse_tree[1][2][3])
        elif input_entry == 'function_parameter_list':
            self.execute = (parse_tree[1])
        elif input_entry == 'loop_statement':
            if len(parse_tree) == 5:
                self.execute = (parse_tree[1][2][4])
            elif len(parse_tree) == 6:
                self.execute = (parse_tree[1][2][3][4][5])
            elif len(parse_tree) == 9:
                self.excute = (parse_tree[1][2][4][6][8])
        elif input_entry == 'arithmetic_statement':
            self.execute = (parse_tree[1])
        elif input_entry == 'arithmetic_expr':
            left_operand, right_operand = parse_tree[1], parse_tree[3]
            if parse_tree[2] == 'mul_op':
                return self.execute(left_operand) * self.execute(right_operand)
            elif parse_tree[2] == 'div_op':
                return self.execute(left_operand) / self.execute(right_operand)
            elif parse_tree[2] == 'add_op':
                return self.execute(left_operand) + self.execute(right_operand)
            elif parse_tree[2] == 'sub_op':
                return self.execute(left_operand) - self.execute(right_operand)
            elif parse_tree[2] == 'expo_op':
                return self.execute(left_operand) ** self.execute(right_operand)
            if len(parse_tree) == 4:
                self.execute = (parse_tree[2][1][3])
            elif len(parse_tree) == 2:
                self.execute = (parse_tree[1])
        elif input_entry == 'arithmetic_op':
            self.execute = (parse_tree[1])
        elif input_entry == 'data_literal':
            if parse_tree[1] == 'int_literal':
                value = int(parse_tree[1])
                return value
            elif parse_tree[1] == 'float_literal':
                value = float(parse_tree[1])
                return value
            elif parse_tree[1] == 'char_literal':
                value = str(parse_tree[1])
                return value
            elif parse_tree[1] == 'string_literal':
                value = str(parse_tree[1])
                return value

    def evaluate_expression(self, expression):
        if isinstance(expression, tuple):
            return self.execute(expression)
        elif isinstance(expression, int) or isinstance(expression, float) or isinstance(expression, str):
            return expression
        pass
