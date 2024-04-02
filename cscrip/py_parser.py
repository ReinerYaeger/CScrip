import ply.yacc as yacc

# Tokens from the lexer
from lex import tokens, lexer
# from ply_semantics import semantic_node
from semantics import semantic

precedence = (
    ('nonassoc', 'left_par_op', 'right_par_op'),  # Parentheses
    ('left', 'expo_op'),  # Exponents
    ('left', 'mul_op', 'div_op'),  # Multiplication and Division
    ('left', 'add_op', 'sub_op'),  # Addition and Subtraction
    ('nonassoc', 'assign_op'),  # Assignment
)


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
    p[0] = ('list_structure', p[1])


def p_program(p):
    '''program : type_declaration main_statement left_curl_op statement right_curl_op
               | type_declaration main_statement left_par_op type_declaration identifier right_par_op left_curl_op statement right_curl_op
               '''
    if len(p) <= 6:
        p[0] = ('program', p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = ('program', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])


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
                 | return_statement identifier
                 | return_statement
                 '''
    p[0] = p[1]


def p_conditional_statement(p):
    '''conditional_statement : if_block
                                | if_block elif_block
                                | if_block elif_block else_block
                                | if_block else_block
                                | left_par_op inequalities right_par_op
                              | left_par_op inequalities right_par_op question_op left_curl_op statement colon_statement statement right_curl_op
                            '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1], p[2]
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
    p[0] = p[1], p[3]


def p_elif_block(p):
    '''elif_block : elif_statement inequalities left_curl_op statement right_curl_op'''
    p[0] = ('elif_block', p[1], p[2], p[4])


def p_inequalities(p):
    '''inequalities : literal_or_identifier inequalities_sym  literal_or_identifier'''

    if len(p) == 4:
        p[0] = ('inequalities', p[2], p[1], p[3])
    else:
        print(f"There is an with the expected range: p[{str(len(p))}] was given")


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


def p_function_parameter(p):
    ''' function_parameter  : literal_or_identifier
                            | function_parameter_list
                            | left_par_op function_parameter right_par_op
                            |left_par_op right_par_op
                            '''
    if len(p) == 2:
        p[0] = (p[1])
    elif len(p) == 4:
        p[0] = (p[1], p[2], p[3])


def p_function_parameter_list(p):
    ''' function_parameter_list : function_parameter comma_statement literal_or_identifier '''
    p[0] = (p[1], p[2], p[3])


def p_literal_or_identifier(p):
    '''literal_or_identifier : identifier
                             | data_literal'''
    p[0] = p[1]


def p_function_call_statement(p):
    '''function_call_statement : identifier left_par_op function_parameter  right_par_op '''
    p[0] = p[1]


def p_loop_statement(p):
    '''loop_statement : while_statement inequalities left_curl_op statement right_curl_op
                      | for_statement arithmetic_statement semi_colon_statement inequalities semi_colon_statement arithmetic_statement left_curl_op statement right_curl_op
                      | for_statement semi_colon_statement semi_colon_statement left_curl_op statement right_curl_op
                      '''
    if len(p) == 5:
        p[0] = ('loop_statement', p[1], p[2], p[4])
    if len(p) == 6:
        p[0] = ('loop_statement', p[1], p[2], p[3], p[4], p[5])
    elif len(p) == 9:
        p[0] = ('loop_statement', p[1], p[2], p[4], p[6], p[8])


def p_arithmetic_statement(p):
    '''arithmetic_statement : arithmetic_expr'''
    p[0] = p[1]


def p_arithmetic_expr(p):
    '''arithmetic_expr : identifier assign_op arithmetic_expr
                       | arithmetic_expr arithmetic_op arithmetic_expr
                       | left_par_op arithmetic_expr right_par_op
                       | literal_or_identifier
                       | identifier assign_op function_call_statement'''
    if len(p) == 4:  # Handle assignment
        p[0] = (p[2], p[1], p[3])  # Return a tuple representing the assignment operation
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2], p[1], p[3]  # Construct an arithmetic expression tuple


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
    print("Syntax error in input!")


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
    ast = semantic(parsed_expression)
    print("Interpreter result:", ast)
