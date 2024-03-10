import ply.yacc as yacc
from ply_lexer import tokens, content

# Symbol Table
symbol_table = {}

precedence = (
    ('left', 'ADD_OP', 'SUB_OP'),
    ('left', 'MUL_OP', 'DIV_OP')
)


def p_program_definition(p):
    """program : function"""
    p[0] = p[1]


def p_function(p):
    """function : TYPE IDENTIFIER '(' ')' '{' statement '}'"""
    p[0] = ('function', p[1], p[2], p[7])


def p_statement(p):
    """statement : assignment_statement
                 | expression"""
    p[0] = p[1]


def p_assignment_statement(p):
    """assignment_statement : IDENTIFIER EQUIVALENT_OP expression SEMI_COLON_STATEMENT"""
    p[0] = ('EQUIVALENT_OP', p[1], p[3])


def p_expression(p):
    """expression : EXPRESSION
                  | EXPRESSION ADD_OP EXPRESSION"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]


# def p_expression(p):
#     """expression : EXPRESSION ADD_OP EXPRESSION
#                   | EXPRESSION SUB_OP EXPRESSION
#                   | EXPRESSION MUL_OP EXPRESSION
#                   | EXPRESSION DIV_OP EXPRESSION
#                   | TERM"""
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         if p[2] == '+':
#             p[0] = p[1] + p[3]
#         elif p[2] == '-':
#             p[0] = p[1] - p[3]
#         elif p[2] == '*':
#             p[0] = p[1] * p[3]
#         elif p[2] == '/':
#             p[0] = p[1] / p[3]


# Error handling
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        print("Input content:", content)
        result = parser.parse(content)
        print(result)
        break  # Exit the loop after parsing the content once
    except EOFError:
        break
