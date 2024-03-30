def semantic(p):
    if isinstance(p, tuple):
        if p[0] == 'program':
            if len(p) == 6:
                return semantic(p[1]), semantic(p[2]), semantic(p[3]), semantic(p[4]), semantic(p[5])
            elif len(p) == 10:
                return semantic(p[1]), p[2], p[3], semantic(p[4]), semantic(p[5]), p[6], p[7], p[8], semantic(p[9])
            else:
                print("Error: Unexpected structure for program production:", p)
                return None
        elif p[0] == 'conditional_statement':
            if len(p) == 2:
                return semantic(p[1])
            elif len(p) == 4:
                return semantic(p[1]), semantic(p[2]), semantic(p[3])
            elif len(p) > 6:
                return semantic(p[1]), semantic(p[2]), semantic(p[4]), semantic(p[5]), semantic(p[6])
            else:
                print("Error: Unexpected structure for conditional_statement production:", p)
                return None
        elif p[0] == 'if_block':
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
                    print("Error: Unsupported comparison operator:", operator)
                    return None
                if condition_result:
                    return semantic(statement)
                else:
                    return None
            else:
                print("Error: Invalid condition in if block:", condition)
                return None
        elif p[0] == 'else_block':
            if len(p) == 4:
                # Handle the case of if_block with else statement
                if_block = semantic(p[1])
                else_statement = p[2]
                statement = p[3]
                # Check if if_block evaluated to None
                if if_block is None:
                    # Evaluate else statement
                    return semantic(statement)
                else:
                    # If if_block is not None, return its result
                    return if_block
            else:
                print("Error: Unexpected structure for else_block production:", p)
                return None
        elif p[0] == 'elif_block':
            # Handle elif_block production
            elif_statement = p[1]
            condition = p[2]
            statement = p[3]

            # Ensure condition is a tuple and its first element is 'inequalities'
            if isinstance(condition, tuple) and condition[0] == 'inequalities':
                operator = condition[1]
                left_operand = condition[2]
                right_operand = condition[3]

                # Evaluate the condition based on the operator
                if operator == '>':
                    condition_result = left_operand > right_operand
                elif operator == '<':
                    condition_result = left_operand < right_operand
                # Add other comparison operators as needed

                # Execute the statement if the condition is true
                if condition_result:
                    return semantic(statement)
                else:
                    return None  # Condition is false, return None
            else:
                print("Error: Invalid condition in elif block:", condition)
                return None
        elif p[0] == 'function_parameter':
            # Handle function_parameter
            if len(p) == 2:
                return semantic(p[1])
            elif len(p) == 4:
                return p[1], semantic(p[2]), p[3]
            else:
                print("Error: Unexpected structure for function_parameter production:", p)
                return None
        elif p[0] == 'function_parameter_list':
            return semantic(p[1]), semantic(p[2]), semantic(p[3])
        elif p[0] == 'loop_statement':
            # Handle loop_statement
            if len(p) == 6:  # While loop without inequalities
                return p[1], semantic(p[2]), p[3], semantic(p[4]), p[5]
            elif len(p) == 9:  # For loop with inequalities
                condition = p[2]  # Get the loop condition
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
                        return semantic(statement)
                    else:
                        return None  # Condition is false, return None
                else:
                    print("Error: Invalid condition in loop statement:", condition)
                    return None
            else:
                print("Error: Unexpected structure for loop_statement production:", p)
                return None
        elif p[0] == '=':
            variable = p[1]  # Get the variable name
            value = semantic(p[2])  # Get the value of the arithmetic expression
            print("Assigning", value, "to", variable)
            return variable, '=', value
        elif len(p) == 2:  # Literal or identifier
            return semantic(p[1])
        elif p[0] == '+':
            left_operand = semantic(p[1])
            right_operand = semantic(p[2])
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                return left_operand + right_operand
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        elif p[0] == '-':
            left_operand = semantic(p[1])
            right_operand = semantic(p[2])
            if isinstance(left_operand, (int, float)) and isinstance(right_operand, (int, float)):
                return left_operand - right_operand
            else:
                print("Error: Non-numeric operands for addition:", left_operand, right_operand)
                return None
        print("Error: Unsupported operator:", p[0])
        return None
    elif isinstance(p, int) or isinstance(p, float) or isinstance(p, str):
        return p
