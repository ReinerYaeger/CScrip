def semantic_node(p, symbol_table):
    if isinstance(p, tuple):
        if p[0] == 'program':
            return semantic_program(p, symbol_table)
        elif p[0] == 'conditional_statement':
            return semantic_conditional(p, symbol_table)
        elif p[0] == 'elif_block':
            return semantic_elif_block(p, symbol_table)
        elif p[0] == 'function_declaration_statement':
            return semantic_function_declaration_statement(p, symbol_table)
        elif p[0] == 'function_call_statement':
            return semantic_function_call_statement(p, symbol_table)
        elif p[0] == 'loop_statement':
            return semantic_loop_statement(p, symbol_table)
        elif p[0] == 'arithmetic_expr':
            return semantic_arithmetic_expr(p, symbol_table)
        elif p[0] == 'return_statement':
            return semantic_return_statement(p, symbol_table)
        else:
            print("Error: Unable to analyze parse tree:", p)
            return None
    elif isinstance(p, (int, float)):
        return p
    elif isinstance(p, str):
        if p in symbol_table:  # Variable lookup
            return symbol_table[p]
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
    print("Processing:", p)
    if isinstance(p, tuple):
        if len(p) == 2:
            semantic = semantic_if_block(p[1], symbol_table)
            return semantic
        elif len(p) == 3:
            if_statement = semantic_if_block(p[1], symbol_table)
            if not if_statement:
                semantic = semantic_else_block(p[2], symbol_table)
                return semantic
            elif p[0] == "elif_block":
                elif_statement = semantic_elif_block(p[1], symbol_table)
                if not elif_statement:
                    semantic = semantic_else_block(p[2], symbol_table)
                    return semantic
        elif len(p) == 4:
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
                return semantic_node(statement, symbol_table)
            else:
                return False
        else:
            return "Error: Invalid condition in if block:", condition
    else:
        return "Error: Unexpected structure for if_block production:", p


def semantic_else_block(p, symbol_table):
    if isinstance(p, tuple):
        statement = p[2]
        return semantic_node(statement, symbol_table)  # Return the evaluated result of the else block
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


def semantic_function_declaration_statement(p, symbol_table):
    if isinstance(p, tuple):
        function_name = p[1]
        parameters = semantic_function_parameter(p[3], symbol_table)
        statements = p[6]
        if function_name in symbol_table:
            return f"Error: Function '{function_name}' is already defined."
        # Store the function object directly in the symbol table
        symbol_table[function_name] = (function_name, parameters, statements)


def semantic_function_parameter(p, symbol_table):
    if len(p) == 1:
        # Single parameter case
        variable = p[0]
        if variable not in symbol_table:
            symbol_table[variable] = None  # Add parameter to symbol table with None value
        return variable
    elif len(p) == 4:
        first_parameter = p[0]
        remaining_parameters = p[2]
        if isinstance(remaining_parameters, tuple):
            # Concatenate parameters
            parameters = (first_parameter,) + remaining_parameters
            # Update symbol table with each parameter
            for param in parameters:
                if param not in symbol_table:
                    symbol_table[param] = None  # Add parameter to symbol table with None value
            return parameters
        else:
            # Two parameters case
            if first_parameter not in symbol_table:
                symbol_table[first_parameter] = None
            if remaining_parameters not in symbol_table:
                symbol_table[remaining_parameters] = None
            return first_parameter, remaining_parameters
    else:
        return None  # Invalid syntax


def semantic_function_call_statement(p, symbol_table):
    if len(p) == 5:
        function_name = p[1]  # Get the name of the function being called
        parameters = p[3]  # Get the semantic interpretation of parameters
        # Check if the function exists in the symbol table
        if function_name in symbol_table:
            # Retrieve the function information from the symbol table
            function_info = symbol_table[function_name]
            if callable(function_info[0]):
                result = function_info[0](*parameters)
                return result
        else:
            return f"Error: Function '{function_name}' is not defined."
    else:
        return "Error: Invalid function call statement syntax."


def semantic_arithmetic_statement(p, symbol_table):
    return semantic_arithmetic_statement(p[1], symbol_table)


def semantic_loop_statement(p, symbol_table):
    if isinstance(p, tuple):
        if len(p) < 5:
            while_statement = p[1]
            condition = p[2]
            statement = p[3]
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
                    return semantic_node(statement, symbol_table)
                else:
                    return "Error: Unsupported Statement"
            else:
                return "Error: Invalid condition in loop_statement:", condition
        elif len(p) <= 5:
            for_statement = p[1]
            arithmetic_statement = p[2]
            statement = p[4]
            initialization = semantic_arithmetic_expr(arithmetic_statement, symbol_table)
            if initialization:
                # Execute the loop body exactly once
                result = semantic_arithmetic_expr(statement, symbol_table)
                return result
        elif len(p) <= 10:  # For loop with inequalities
            for_statements = p[1]
            arithmetic_statements = semantic_arithmetic_expr(p[2], symbol_table)
            conditions = p[3]
            statement = p[5]
            increment_decrement = p[4]  # Increment/decrement statement
            if isinstance(conditions, tuple) and conditions[0] == 'inequalities':
                operator = conditions[1]
                left_operand = semantic_node(conditions[2], symbol_table)
                right_operand = semantic_node(conditions[3], symbol_table)
                condition_result = None

                # Evaluate condition
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
                results = []
                while condition_result:  # Use a while loop to repeat until condition is False
                    if condition_result:
                        # Execute loop body
                        result = semantic_node(statement, symbol_table)
                        results.append(result)
                    # Evaluate increment/decrement statement
                    semantic_arithmetic_expr(increment_decrement, symbol_table)
                    # Re-evaluate condition
                    left_operand = semantic_node(conditions[2], symbol_table)
                    right_operand = semantic_node(conditions[3], symbol_table)
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
                return ', '.join(map(str, results))
            else:
                print("Error: Invalid condition in loop statement:", conditions)
                return None
    else:
        return "Error: Unexpected structure for loop production:", p


def semantic_arithmetic_expr(p, symbol_table):
    if isinstance(p, tuple):
        assign_op = p[1]
        if assign_op == '=':
            variable = p[2]
            value = semantic_node(p[3], symbol_table)
            symbol_table[variable] = value
            print("Assigning", value, "to", variable)
            return value
        if len(p) == 2:
            if isinstance(p[0], str) or isinstance(p[0], int):
                if p[0] in symbol_table:
                    return symbol_table[p[0]]
                else:
                    print(f"Error: Variable {p[0]} is not defined.")
                    return None
            else:
                return semantic_arithmetic_expr(p[0], symbol_table)
        elif p[1] == '+':
            left_operand = semantic_node(p[2], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                return left_operand + right_operand
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        elif p[1] == '-':
            left_operand = semantic_node(p[2], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                return left_operand - right_operand
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        elif p[1] == '*':
            left_operand = semantic_node(p[2], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                return left_operand * right_operand
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        elif p[1] == '/':
            left_operand = semantic_node(p[0], symbol_table)
            right_operand = semantic_node(p[1], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                if left_operand != 0:
                    return left_operand / right_operand
                else:
                    print("Error: Unable to divide by zero:", left_operand)
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        elif p[1] == '**':
            left_operand = semantic_node(p[2], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                return left_operand ** right_operand
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        elif p[2] in ('--', '++'):
            variable = p[1]
            if variable in symbol_table:
                if p[2] == '--':
                    symbol_table[variable] -= 1
                elif p[2] == '++':
                    symbol_table[variable] += 1
                return symbol_table[variable]
            else:
                return f"Error: Variable '{variable}' not defined"
        print("Error: Unsupported operator:", p[0])
        return None
    else:
        print("Error: Unexpected structure for arithmetic_expr production:", p)
        return None


def semantic_return_statement(p, symbol_table):
    if isinstance(p, tuple):
        value = p[2]
        if isinstance(value, str):
            # If the value is a variable name
            if value in symbol_table:
                return symbol_table[value]
            else:
                print(f"Error: Variable '{value}' not defined.")
                return None
        else:
            # If the value is an arithmetic expression
            return semantic_arithmetic_expr(value, symbol_table)
    else:
        print("Error: Invalid return statement structure.")
        return None


def semantic_break_statement():
    return "break"
