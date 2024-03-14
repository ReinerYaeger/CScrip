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


def p_program(p):
    '''program : type_declaration main_statement left_curl_op statement right_curl_op
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
    '''conditional_statement : empty'''
    p[0] = p[1]


def p_inequalities(p):
    '''inequalities :  inequalities_sym identifier
                    | literal_or_identifier inequalities_sym  literal_or_identifier'''


def p_literal_or_identifier(p):
    '''literal_or_identifier : identifier
                             | data_literal'''
    p[0] = p[1]


def p_inequalities_sym(p):
    '''inequalities_sym : equivalent_op
                        | less_or_eq_op
                        | great_or_eq_op
                        | less_op
                        | great_op
                        | '''
    p[0] = p[1]


def p_function_call_statement(p):
    '''function_call_statement : empty'''
    p[0] = p[1]


def p_loop_statement(p):
    '''loop_statement : while_statement inequalities left_curl_op statement right_curl_op
                      | for_statement semi_colon_statement semi_colon_statement left_curl_op statement right_curl_op
                      | for_statement arithmetic_statement semi_colon_statement inequalities semi_colon_statement arithmetic_statement left_curl_op statement right_curl_op
                      | do_statement inequalities left_curl_op statement right_curl_op'''


def p_arithmetic_statement(p):
    '''arithmetic_statement : arithmetic_expr'''
    p[0] = p[1]


def p_arithmetic_expr(p):
    '''arithmetic_expr : literal_or_identifier assign_op arithmetic_expr
                       | arithmetic_expr arithmetic_op arithmetic_expr
                       | left_par_op arithmetic_expr right_par_op
                       | literal_or_identifier'''
    if len(p) == 4:  # Handle assignment
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])


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
                    | bool_literal
                    | char_literal
                    | string_literal'''
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
