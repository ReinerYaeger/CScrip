import ply.yacc as yacc

# Tokens from the lexer
from lex import tokens, lexer
from ply_semantics import semantic_node

precedence = (
    ('nonassoc', 'left_par_op', 'right_par_op'),  # Parentheses
    ('left', 'expo_op'),  # Exponents
    ('left', 'mul_op', 'div_op'),  # Multiplication and Division
    ('left', 'add_op', 'sub_op'),  # Addition and Subtraction
    ('nonassoc', 'assign_op'),  # Assignment
)

symbol_table = {}


def p_program_start(p):
    ''' program_start : program
                      | statement
                      | data_structure
                      '''
    p[0] = p[1]


def p_data_structure(p):
    '''data_structure : class
                      | struct
                      | list_structure
                      | array
                      | empty'''
    if len(p) > 1:
        p[0] = p[1]


def p_list_structure(p):
    ''' list_structure : list'''
    p[0] = p[1]


# def p_list(p):
#     ''' list : type_declaration identifier left_square_op statement right_square_op'''
#     p[0] = p[1], p[2], p[3], p[4], p[5]


def p_program(p):
    '''program : type_declaration main_statement left_curl_op statement right_curl_op
               | type_declaration main_statement left_par_op type_declaration identifier right_par_op left_curl_op statement right_curl_op
               '''
    if len(p) <= 6:
        p[0] = ('program', p[1], p[2], p[3], p[4], p[5])
        # Update symbol table with variable name and type
        if p[1][1] not in symbol_table:
            symbol_table[p[1][1]] = p[1][0]
    else:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])
        # Update symbol table with variable name and type
        if p[1][1] not in symbol_table:
            symbol_table[p[1][1]] = p[1][0]


def p_type_declaration(p):
    '''type_declaration : int_declaration
                        | float_declaration
                        | double_declaration
                        | string_declaration
                        | char_declaration'''
    p[0] = p[1]


def p_statement(p):
    '''statement : function_call_statement
                 | conditional_statement
                 | loop_statement
                 | arithmetic_statement
                 | break_statement
                 | return_state
                 | function_declaration_statement
                 | printed_statement
                 '''
    p[0] = p[1]


def p_printed_statement(p):
    '''printed_statement : print_statement literal_or_identifier
                         | print_statement literal_or_identifier comma_statement identifier'''
    if len(p) == 3:
        p[0] = ('printed_statement', p[1], p[2])
    elif len(p) == 5:
        p[0] = ('printed_statement', p[1], p[2], p[3], p[4])


def p_return_statement(p):
    '''return_state : return_statement literal_or_identifier
                    | return_statement statement'''
    p[0] = ('return_statement', p[1], p[2])


def p_conditional_statement(p):
    '''conditional_statement : if_block
                                | if_block elif_block
                                | if_block else_block
                                | left_par_op inequalities right_par_op
                              | left_par_op inequalities right_par_op question_op left_curl_op statement colon_statement statement right_curl_op
                            '''
    if len(p) == 2:
        p[0] = ('conditional_statement', p[1])
    elif len(p) == 3:
        p[0] = ('conditional_statement', p[1], p[2])
    elif len(p) == 4:
        p[0] = p[1], p[2], p[3]
    elif len(p) > 8:
        p[0] = p[1], p[2], p[4], p[5], p[6]
    else:
        print(f"There is an with the expected range: p[{str(len(p))}] was given")


def p_if_block(p):
    ''' if_block : if_statement inequalities left_curl_op statement right_curl_op'''

    p[0] = ('if_block', p[1], p[2], p[3], p[4], p[5])


def p_else_block(p):
    '''else_block : else_statement left_curl_op statement right_curl_op
                  '''
    p[0] = ('else_block', p[1], p[3])


def p_elif_block(p):
    '''elif_block : elif_statement inequalities left_curl_op statement right_curl_op'''
    p[0] = ('elif_block', p[1], p[2], p[4])


def p_inequalities(p):
    '''inequalities : literal_or_identifier inequalities_sym  literal_or_identifier'''

    if len(p) == 4:
        p[0] = ('inequalities', p[2], p[1], p[3])
    else:
        return f"There is an with the expected range: p[{str(len(p))}] was given"


def p_inequalities_sym(p):
    '''inequalities_sym : equivalent_op
                        | less_or_eq_op
                        | great_or_eq_op
                        | less_op
                        | great_op
                        | and
                        | or
                        | bool_literal
                        | not_equal
                        | '''
    p[0] = (p[1])


def p_function_declaration_statement(p):
    '''function_declaration_statement : literal_or_identifier left_par_op function_parameter right_par_op left_curl_op statement right_curl_op'''
    p[0] = ('function_declaration_statement', p[1], p[2], p[3], p[4], p[5], p[6], p[7])


def p_function_parameter(p):
    ''' function_parameter  : literal_or_identifier
                            | literal_or_identifier comma_statement function_parameter
                            '''
    if len(p) == 2:
        p[0] = (p[1])
    elif len(p) == 3:
        p[0] = (p[1], p[2], p[3])


def p_literal_or_identifier(p):
    '''literal_or_identifier : identifier
                             | data_literal'''
    p[0] = p[1]


def p_function_call_statement(p):
    '''function_call_statement : literal_or_identifier left_par_op function_parameter right_par_op  '''
    p[0] = ('function_call_statement', p[1], p[2], p[3], p[4])


def p_loop_statement(p):
    '''loop_statement : while_statement inequalities left_curl_op statement right_curl_op
                      | for_statement arithmetic_statement semi_colon_statement left_curl_op statement right_curl_op
                      | for_statement arithmetic_statement semi_colon_statement inequalities semi_colon_statement arithmetic_statement left_curl_op statement right_curl_op
                      '''
    if len(p) == 6:
        p[0] = ('loop_statement', p[1], p[2], p[4])
    elif len(p) == 7:
        p[0] = ('loop_statement', p[1], p[2], p[3], p[5], p[6])
    elif len(p) == 10:
        p[0] = ('loop_statement', p[1], p[2], p[4], p[6], p[8])
    else:
        return "Invalid loop statement"


def p_arithmetic_statement(p):
    '''arithmetic_statement : arithmetic_expr
                            | unary_op'''
    p[0] = p[1]


def p_unary_op(p):
    '''unary_op : identifier increment
                | identifier decrement'''
    p[0] = ('unary_op', p[1], p[2])


def p_arithmetic_expr(p):
    '''arithmetic_expr : identifier assign_op arithmetic_expr
                       | arithmetic_expr arithmetic_op arithmetic_expr
                       | left_par_op arithmetic_expr right_par_op
                       | literal_or_identifier
                       | identifier assign_op function_call_statement'''
    if len(p) == 4:  # Handle assignment
        p[0] = ('arithmetic_expr', p[2], p[1], p[3])
        if p[1] not in symbol_table:
            symbol_table[p[1]] = None
    elif len(p) == 2:
        p[0] = (p[1])
    else:
        p[0] = p[2], p[1], p[3]


def p_arithmetic_op(p):
    '''arithmetic_op : expo_op
                    | mul_op
                    | div_op
                    | add_op
                     | sub_op
                     '''
    p[0] = p[1]


def p_data_literal(p):
    '''data_literal : int_literal
                    | float_literal
                    | double_literal
                    | char_literal
                    | string_literal'''
    p[0] = p[1]


def p_empty(p):
    ''' empty : '''
    p[0] = ()


def p_error(p):
    '''error : empty'''
    return "Syntax error in input!"


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input(">>>  ")
    except EOFError:
        break
    if not s:
        continue

    lexer.input(s)
    for token in lexer:
        print(token)

    parsed_expression = parser.parse(s)
    print("Parsed expression:", parsed_expression)

    # Pass the root node of the parse tree to the semantic analysis function
    ast = semantic_node(parsed_expression, symbol_table)
    print("Interpreter result:", ast)
