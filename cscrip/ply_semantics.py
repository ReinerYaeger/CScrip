def semantic_node(p, symbol_table):
    if isinstance(p, tuple):
        if p[0] == 'program':
            return semantic_program(p, symbol_table)
        elif p[0] == 'conditional_statement':
            return semantic_conditional(p, symbol_table)
        elif p[0] == 'if_block':
            return semantic_if_block(p, symbol_table)
        elif p[0] == 'else_block':
            return semantic_else_block(p, symbol_table)
        elif p[0] == 'elif_block':
            return semantic_elif_block(p, symbol_table)
        elif p[0] == 'function_parameter':
            return semantic_function_parameter_list(p, symbol_table)
        elif p[0] == 'function_parameter_list':
            return semantic_function_parameter_list(p, symbol_table)
        elif p[0] == 'loop_statement':
            return semantic_loop_statement(p, symbol_table)
        elif p[0] == 'arithmetic_expr':
            return semantic_arithmetic_expr(p, symbol_table)
        else:
            print("Error: Unable to analyze parse tree:", p)
            return None
    elif isinstance(p, (int, float, str)):
        return p
    else:
        return "Error: Unexpected type in parse tree:", type(p)


def semantic_program(p, symbol_table):
    if isinstance(p, tuple):
        if len(p) == 6:
            return semantic_program(p[4], symbol_table)
        elif len(p) == 10:
            return semantic_program(p[8], symbol_table)
    else:
        return "Error: Unexpected structure for program production:", p


def semantic_conditional(p, symbol_table):
    if isinstance(p, tuple):
        if len(p) == 1:
            return semantic_conditional(p[1], symbol_table)
        elif len(p) == 2:
            return semantic_conditional(p[1], symbol_table), semantic_conditional(p[2], symbol_table)
        elif len(p) == 3:
            return (semantic_conditional(p[1], symbol_table), semantic_conditional(p[2], symbol_table),
                    semantic_conditional(p[3], symbol_table))
        elif len(p) > 8:
            return (semantic_conditional(p[1], symbol_table), semantic_conditional(p[2], symbol_table),
                    semantic_conditional(p[3], symbol_table), semantic_conditional(p[4], symbol_table),
                    semantic_conditional(p[5], symbol_table), semantic_conditional(p[6], symbol_table))
    else:
        return "Error: Unexpected structure for conditional production:", p


def semantic_if_block(p, symbol_table):
    if isinstance(p, tuple):
        if_statement = p[1]
        condition = p[2]
        statement = p[4]
        if isinstance(condition, tuple) and condition[0] == 'inequalities':
            operator = condition[1]
            left_operand = condition[2]
            right_operand = condition[3]
            condition_result = None
            if operator == '<':
                condition_result = left_operand < right_operand
            elif operator == '>':
                condition_result = left_operand > right_operand
            elif operator == '<=':
                condition_result = left_operand <= right_operand
            elif operator == '>=':
                condition_result = left_operand >= right_operand
            elif operator == '==':
                condition_result = left_operand == right_operand
            elif operator == '!=':
                condition_result = left_operand != right_operand
            else:
                return "Error: Unsupported comparison operator:", operator

            if condition_result:
                return semantic_if_block(statement, symbol_table)
            else:
                return "Error: Unsupported Statement", False
        else:
            return "Error: Invalid condition in if block:", condition
    else:
        return "Error: Unexpected structure for if_block production:", p


def semantic_else_block(p, symbol_table):
    if isinstance(p, tuple):
        if len(p) == 4:
            if_statement = semantic_if_block(p[1], symbol_table)
            else_statement = p[2]
            statement = p[4]
            if if_statement is False:
                return semantic_elif_block(statement, symbol_table)
            else:
                return if_statement
    else:
        return "Error: Unexpected structure for else_block production:", p


def semantic_elif_block(p, symbol_table):
    if isinstance(p, tuple):
        elif_statement = p[1]
        condition = p[2]
        statement = p[4]
        condition_result = None
        if isinstance(condition, tuple) and condition[0] == 'inequalities':
            operator = condition[1]
            left_operand = condition[2]
            right_operand = condition[3]
            condition_result = None
            if operator == '<':
                condition_result = left_operand < right_operand
            elif operator == '>':
                condition_result = left_operand > right_operand
            elif operator == '<=':
                condition_result = left_operand <= right_operand
            elif operator == '>=':
                condition_result = left_operand >= right_operand
            elif operator == '==':
                condition_result = left_operand == right_operand
            elif operator == '!=':
                condition_result = left_operand != right_operand
            else:
                return "Error: Unsupported comparison operator:", operator
            if condition:
                return semantic_else_block(statement, symbol_table)
            else:
                return "Error: Unsupported Statement"
        else:
            return "Error: Invalid condition in elif block:", condition
    else:
        return "Error: Unexpected structure for elif_block production:", p


def semantic_function_parameter_list(p, symbol_table):
    if isinstance(p, tuple):
        return (semantic_function_parameter_list(p[1], symbol_table), semantic_function_parameter_list(p[2],
                                                                                                       symbol_table),
                semantic_function_parameter_list(p[3], symbol_table))
    else:
        return "Error: Unexpected structure for function_parameter_list production:", p


def semantic_arithmetic_statement(p, symbol_table):
    return semantic_arithmetic_statement(p[1], symbol_table)


def semantic_loop_statement(p, symbol_table):
    if isinstance(p, tuple):
        if len(p) == 5:
            condition = p[2]
            statement = p[4]
            if isinstance(condition, tuple) and condition[0] == 'inequalities':
                operator = condition[1]
                left_operand = condition[2]
                right_operand = condition[3]
                condition_result = None
                if operator == '<':
                    condition_result = left_operand < right_operand
                elif operator == '>':
                    condition_result = left_operand > right_operand
                elif operator == '<=':
                    condition_result = left_operand <= right_operand
                elif operator == '>=':
                    condition_result = left_operand >= right_operand
                elif operator == '==':
                    condition_result = left_operand == right_operand
                elif operator == '!=':
                    condition_result = left_operand != right_operand
                else:
                    print("Error: Unsupported comparison operator:", operator)
                    return None
                if condition_result:
                    return semantic_loop_statement(statement, symbol_table)
                else:
                    return "Error: Unsupported Statement"
            else:
                return "Error: Invalid condition in loop_statement:", condition
        elif len(p) == 6:
            arithmetic_statement = p[2]
            statement = p[5]

            initialization = semantic_arithmetic_statement(arithmetic_statement, symbol_table)
            result_loop = None
            while initialization:
                result_loop = semantic_loop_statement(statement, symbol_table)
                initialization = semantic_node(p[4], symbol_table)
            return result_loop
        elif len(p) == 9:  # For loop with inequalities
            initialization = p[1]
            condition = p[2]  # Get the loop condition
            arithmetic_statement = p[6]
            statement = p[8]
            if isinstance(condition, tuple) and condition[0] == 'inequalities':
                operator = condition[1]
                left_operand = condition[2]
                right_operand = condition[3]
                condition_result = None
                if operator == '<':
                    condition_result = left_operand < right_operand
                elif operator == '>':
                    condition_result = left_operand > right_operand
                elif operator == '<=':
                    condition_result = left_operand <= right_operand
                elif operator == '>=':
                    condition_result = left_operand >= right_operand
                elif operator == '==':
                    condition_result = left_operand == right_operand
                elif operator == '!=':
                    condition_result = left_operand != right_operand
                else:
                    print("Error: Unsupported comparison operator:", operator)
                    return None
                if condition_result:
                    initialization = semantic_arithmetic_statement(arithmetic_statement, symbol_table)
                    result_loop = None
                    while initialization:
                        result_loop = semantic_loop_statement(statement, symbol_table)
                        initialization = semantic_node(p[7], symbol_table)
                    return result_loop
                else:
                    return None  # Condition is false, return None
            else:
                print("Error: Invalid condition in loop statement:", condition)
                return None
    else:
        return "Error: Unexpected structure for loop production:", p


def semantic_arithmetic_expr(p, symbol_table):
    print("Processing:", p)
    if isinstance(p, tuple):
        if len(p) <= 4:
            assign_op = p[1]
            if assign_op == '=':
                variable = p[2]
                value = p[3]
                print("Assigning", value, "to", variable)
                symbol_table[variable] = value
                return value
        elif len(p) == 2:
            if isinstance(p[0], str) or isinstance(p[0], int):
                if p[0] in symbol_table:
                    return symbol_table[p[0]]
                else:
                    print(f"Error: Variable {p[0]} is not defined.")
                    return None
            else:
                return semantic_arithmetic_expr(p[0], symbol_table)
        else:
            left_operand = semantic_arithmetic_expr(p[1], symbol_table)
            right_operand = semantic_arithmetic_expr(p[2], symbol_table)
            print("Left operand:", left_operand)
            print("Right operand:", right_operand)
            if p[0] == '+':
                result = left_operand + right_operand
                print("Result of addition:", result)
                return result
            elif p[0] == '-':
                result = left_operand - right_operand
                print("Result of subtraction:", result)
                return result
            elif p[0] == '*':
                result = left_operand * right_operand
                print("Result of multiplication:", result)
                return result
            elif p[0] == '/':
                if right_operand != 0:
                    result = left_operand / right_operand
                    print("Result of division:", result)
                    return result
                else:
                    print("Error: Unable to divide by zero.")
                    return None
            elif p[0] == '**':
                result = left_operand ** right_operand
                print("Result of exponentiation:", result)
                return result
            else:
                print("Error: Invalid operation:", p[0])
                return None
    else:
        print("Error: Unexpected structure for arithmetic_expr production:", p)
        return None
