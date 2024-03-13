import ply.yacc as yacc

# Tokens from the lexer
from lex import tokens, lexer


def p_program_start(p):
    ''' program_start : program
                      | arithmetic_statement
                      '''
    p[0] = p[1]


def p_empty(p):
    ''' empty : '''
    p[0] = None


def p_function_declaration(p):
    '''
    program : type_declaration main_statement left_curl_op statement right_curl_op
            | type_declaration main_statement left_par_op type_declaration identifier right_par_op left_curl_op statement right_curl_op
            '''
    if len(p) == 6:
        p[0] = (p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = None


def p_type_declaration(p):
    '''type_declaration : int_declaration
                        | float_declaration
                        | double_declaration
                        | string_declaration
                        | char_declaration'''
    p[0] = p[1]


def p_statement(p):
    '''
    statement : function_call_statement
                | conditional_statement
                | loop_statement
                | arithmetic_statement
                | break_statement
                | return_statement identifier
                | return_statement
                '''
    p[0] = None


def p_conditional_statement(p):
    '''conditional_statement : empty'''
    p[0] = None


def p_function_call_statement(p):
    '''function_call_statement : empty'''
    p[0] = None


def p_loop_statement(p):
    '''loop_statement : empty'''
    p[0] = None


def p_arithmetic_statement(p):
    '''arithmetic_statement :
                    | expression arithmetic_op expression
                    | left_par_op arithmetic_statement right_par_op
                    | data_literal'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])  # Construct a tuple representing the operation
    else:
        p[0] = p[1]


def p_arithmetic_op(p):
    '''arithmetic_op : add_op
                     | sub_op
                     | expo_op
                     | mul_op
                     | div_op'''
    p[0] = p[1]


def p_data_literal(p):
    '''data_literal : int_literal
                    | float_literal
                    | double_literal
                    | bool_literal'''
    p[0] = p[1]

def p_expression(p):
    '''expression : identifier
                  |  data_literal'''
    if len(p) == 3:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == "**":
            p[0] = p[1] ** p[3]
    else:
        p[0] = p[1]


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

    result = parser.parse(s)
    print(result)