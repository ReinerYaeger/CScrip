import ply.yacc as yacc
from ply_lexer import lexer, tokens, content


# Grammar rules
def p_expression(p):
    """
    expression : INT_LITERAL
               | FLOAT_LITERAL
               | term
    """


    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        else:  # p[2] == '-'
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]


def p_term(p):
    """
    term : term MUL_OP factor
         | term DIV_OP factor
         | factor
    """
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        else:  # p[2] == '/'
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]


def p_factor(p):
    """
    factor : NUMBER
           | LEFT_PAR_OP expression RIGHT_PAR_OP
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input")


# Build the parser
parser = yacc.yacc()

with open('test/test.lang', 'r') as file:
    input_expr = file.read()

# Tokenize input
lexer.input(input_expr)

# Parse input
result = parser.parse(lexer=lexer)
print("Result:", result)
