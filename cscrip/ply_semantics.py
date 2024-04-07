def semantic_node(p, symbol_table):
    if isinstance(p, tuple):
        if p[0] == 'program':
            return semantic_program(p, symbol_table)
        elif p[0] == 'conditional_statement':
            return semantic_conditional(p, symbol_table)
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
        elif p[0] == 'printed_statement':
            return semantic_print_statement(p, symbol_table)
        else:
            return "Error: Unable to analyze parse tree:", p
    elif isinstance(p, (int, float)):
        return p
    elif isinstance(p, str):
        if p in symbol_table:  # Variable lookup
            return symbol_table[p]
        else:
            return p
    else:
        return "Error: Unexpected type in parse tree:", type(p)


def semantic_program(p, symbol_table):
    if isinstance(p, tuple):
        if len(p) == 6:
            return semantic_node(p[4], symbol_table)
        elif len(p) == 10:
            return semantic_node(p[8], symbol_table)
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
                block_body = p[2][0]
                conditions = p[2]
                if block_body == 'else_block':
                    semantic = semantic_else_block(conditions, symbol_table)
                    return semantic
                elif block_body == 'elif_block':
                    semantics = semantic_elif_block(conditions, block_body)
                    return semantics
            else:
                semantics = semantic_elif_block(p[2], symbol_table)
                return semantics
        elif len(p) <= 4:
            if_statement = semantic_if_block(p[1], symbol_table)
            return if_statement
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
        statement = p[3]
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
                return semantic_node(statement, symbol_table)
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
        symbol_table[function_name] = {function_name, parameters, statements}


def semantic_function_parameter(p, symbol_table):
    if len(p) == 1:
        # Single parameter case
        variable = p[0]
        if variable not in symbol_table:
            symbol_table[variable] = None  # Add parameter to symbol table with None value
        return variable
    elif len(p) <= 4:
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
            functions = list(function_info)[0]  # Convert set to list and access the first element
            if callable(functions):
                result = function_info(**parameters)
                return result
            else:
                return "Hello"
        else:
            return f"Error: Function '{function_name}' is not defined."
    else:
        return "Error: Invalid function call statement syntax."


def semantic_arithmetic_statement(p, symbol_table):
    return semantic_arithmetic_statement(p[1], symbol_table)


def semantic_loop_statement(p, symbol_table):
    if isinstance(p, tuple):
        local_symbol_table = symbol_table.copy()  # Create a local symbol table based on the parent symbol table
        # Add loop statement to symbol table
        local_symbol_table['loop_statement'] = p
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
                    return "Error: Unsupported comparison operator:", operator
                if condition_result:
                    # Execute loop body with the local symbol table
                    return semantic_node(statement, local_symbol_table)
                else:
                    return "Error: Condition is False"
            else:
                return "Error: Invalid condition in loop_statement:", condition
        elif len(p) <= 5:
            for_statement = p[1]  # For loop without inequalities
            arithmetic_statement = p[2]
            statement = p[4]
            initialization = semantic_arithmetic_expr(arithmetic_statement, local_symbol_table)
            if initialization:
                # Execute the loop body exactly once with the local symbol table
                return semantic_arithmetic_expr(statement, local_symbol_table)
        elif len(p) <= 10:  # For loop with inequalities
            for_statements = p[1]
            arithmetic_statements = semantic_arithmetic_expr(p[2], local_symbol_table)
            conditions = p[3]
            statement = p[5]
            increment_decrement = p[4]  # Increment/decrement statement
            if isinstance(conditions, tuple) and conditions[0] == 'inequalities':
                operator = conditions[1]
                left_operand = semantic_node(conditions[2], local_symbol_table)
                right_operand = semantic_node(conditions[3], local_symbol_table)
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
                    return "Error: Unsupported comparison operator:", operator

                results = []
                while condition_result:  # Use a while loop to repeat until condition is False
                    if condition_result:
                        # Execute loop body with the local symbol table
                        result = semantic_node(statement, local_symbol_table)
                        results.append(result)
                    # Evaluate increment/decrement statement
                    semantic_arithmetic_expr(increment_decrement, local_symbol_table)

                    # Re-evaluate condition
                    left_operand = semantic_node(conditions[2], local_symbol_table)
                    right_operand = semantic_node(conditions[3], local_symbol_table)
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

                return ', '.join(map(str, results))
            else:
                return "Error: Invalid condition in loop statement:", conditions
    else:
        return "Error: Unexpected structure for loop production:", p


def semantic_arithmetic_expr(p, symbol_table):
    if isinstance(p, tuple):
        assign_op = p[2]  # assigning variable to a value
        if assign_op == '=':
            # Handle assignment operation
            variable = p[1]
            value = semantic_node(p[3], symbol_table)
            symbol_table[variable] = value
            print(f"Assigning {value} to {variable}")
            return value
        if len(p) == 2:  # Checking if a value is in the symbol table and resulting the value
            if isinstance(p[0], str) or isinstance(p[0], int) or isinstance(p[0], float):
                if p[0] in symbol_table:
                    return symbol_table[p[0]]
                else:
                    return f"Error: Variable {p[0]} is not defined."
            else:
                return semantic_arithmetic_expr(p[0], symbol_table)
        if len(p) == 5:
            result = None
            assign_op = p[2][2]
            if assign_op == '+':
                left_number = semantic_node(p[2][1], symbol_table)
                right_number = semantic_node(p[2][3], symbol_table)
                if isinstance(left_number, (int, float)) and isinstance(right_number, (int, float)):
                    result = left_number + right_number
                    if isinstance(p[1], str) and p[1] in symbol_table:
                        symbol_table[p[1]] = result
                    return result
                else:
                    semantic_node(p, symbol_table)
            elif assign_op == '-':
                left_number = semantic_node(p[2][1], symbol_table)
                right_number = semantic_node(p[2][3], symbol_table)
                if isinstance(left_number, (int, float)) and isinstance(right_number, (int, float)):
                    result = left_number - right_number
                    if isinstance(p[1], str) and p[1] in symbol_table:
                        symbol_table[p[1]] = result
                    return result
            elif assign_op == '*':
                left_number = semantic_node(p[2][1], symbol_table)
                right_number = semantic_node(p[2][3], symbol_table)
                if isinstance(left_number, (int, float)) and isinstance(right_number, (int, float)):
                    result = left_number * right_number
                    if isinstance(p[1], str) and p[1] in symbol_table:
                        symbol_table[p[1]] = result
                    return result
            elif assign_op == '/':
                left_number = semantic_node(p[2][1], symbol_table)
                right_number = semantic_node(p[2][3], symbol_table)
                if isinstance(left_number, (int, float)) and isinstance(right_number, (int, float)):
                    if left_number != 0:
                        result = left_number / right_number
                        if isinstance(p[1], str) and p[1] in symbol_table:
                            symbol_table[p[1]] = result
                        return result
                    else:
                        return "Error: Unable to divide by zero:", left_number
                else:
                    return "Error: Non-numeric operands for division:", left_number, right_number
            elif assign_op == '**':  # power
                left_number = semantic_node(p[1], symbol_table)
                right_number = semantic_node(p[3], symbol_table)
                if isinstance(left_number, (int, float)) and isinstance(right_number, (int, float)):
                    result = left_number ** right_number
                    if isinstance(p[1], str) and p[1] in symbol_table:
                        symbol_table[p[1]] = result
                    return result
                else:
                    return "Error: Non-numeric operands for addition:", left_number, right_number
        elif p[2] == '+':  # addition
            left_operand = semantic_node(p[2][1], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                result = left_operand + right_operand
                if isinstance(p[1], str) and p[1] in symbol_table:
                    symbol_table[p[1]] = result
                return result
            else:
                return "Error: Non-numeric operands for addition:", left_operand, right_operand
        elif p[2] == '-':  # subtraction
            left_operand = semantic_node(p[1], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                result = left_operand - right_operand
                if isinstance(p[1], str) and p[1] in symbol_table:
                    symbol_table[p[1]] = result
                return result
            else:
                return "Error: Non-numeric operands for addition:", left_operand, right_operand
        elif p[2] == '*':  # multiplication
            left_operand = semantic_node(p[1], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                result = left_operand * right_operand
                if isinstance(p[1], str) and p[1] in symbol_table:
                    symbol_table[p[1]] = result
                return result
            else:
                return "Error: Non-numeric operands for addition:", left_operand, right_operand
        elif p[2] == '/':  # division
            left_operand = semantic_node(p[1], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                if left_operand != 0:
                    result = left_operand / right_operand
                    if isinstance(p[1], str) and p[1] in symbol_table:
                        symbol_table[p[1]] = result
                    return result
                else:
                    return "Error: Unable to divide by zero:", left_operand
            else:
                return "Error: Non-numeric operands for division:", left_operand, right_operand
        elif p[2] == '**':  # power
            left_operand = semantic_node(p[1], symbol_table)
            right_operand = semantic_node(p[3], symbol_table)
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                result = left_operand ** right_operand
                if isinstance(p[1], str) and p[1] in symbol_table:
                    symbol_table[p[1]] = result
                return result
            else:
                return "Error: Non-numeric operands for addition:", left_operand, right_operand
        elif p[2] in ('--', '++'):  # increment and decrement
            variable = p[1]
            if variable in symbol_table:
                if p[2] == '--':
                    symbol_table[variable] -= 1
                elif p[2] == '++':
                    symbol_table[variable] += 1
                return symbol_table[variable]
            else:
                return f"Error: Variable '{variable}' not defined"
        return "Error: Unsupported operator:", p[0]
    else:
        return "Error: Unexpected structure for arithmetic_expr production:", p


def semantic_return_statement(p, symbol_table):
    if isinstance(p, tuple):
        value = p[2]
        if isinstance(value, str):
            # If the value is a variable name
            if value in symbol_table:
                return symbol_table[value]
            else:
                return f"Error: Variable '{value}' not defined."
        else:
            # If the value is an arithmetic expression
            return semantic_arithmetic_expr(value, symbol_table)
    else:
        return "Error: Invalid return statement structure."


def semantic_break_statement(p, loop_stack):
    # Check if there are any loops to break out of
    if loop_stack:
        # Pop the loop from the stack to signify a break out of the innermost loop
        loop_stack.pop()
    else:
        # If there are no loops to break out of, raise an error
        raise SyntaxError("Break statement used outside of loop")


def semantic_print_statement(p, symbol_table):
    if len(p) <= 4:
        printed_content = p[2]
        if printed_content in symbol_table:
            value = symbol_table[printed_content]
            return value
        else:
            return printed_content.strip('"')
    elif len(p) == 5:
        printed_content = p[2]
        printed_variable = p[4]
        if printed_variable in symbol_table:
            value = symbol_table[printed_variable]
            if isinstance(value, int):
                values = str(value)
            else:
                values = value
            return printed_content + ', ' + values
        else:
            return printed_content.strip('"')
    else:
        return "Error: Invalid printed statement syntax."
