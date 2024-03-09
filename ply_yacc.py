import ply.yacc as yacc

from ply_lexer import tokens

# Symbol Table
symbol_table = {}

precedence = (
    ('LEFT', 'INT'),
    ('LEFT', 'IF'),
    ('LEFT', 'ELSE'),
    ('LEFT', 'PLUS', 'MINUS', 'MULTIPLE', 'DIVIDE'),
    ('LEFT', 'WHILE'),
    ('LEFT', 'WHILE')
)


def p_program_definition(p):
    """program: functon"""
    p[0] = p[1]


def p_function(p):
    """function : TYPE IDENTIFIER '(' ')' '{' statements '}"""
    p[0] = ('function', p[1], p[2], p[7])


def p_statements(p):
    """statement : expression SEMICOLON
                 | conditional
                 | function_call"""
    p[0] = p[1]


def p_expression(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression DIVIDE expression
                  | expression MULTIPLE expression
                  | PRINT '(' expression ')'
                  | NUMBER"""
    if len(p) == 4:
        if p[1] == 'print':
            p[0] = ('print', p[3])
        else:
            if p[2] == '+':
                p[0] = p[1] + p[3]
            elif p[2] == '-':
                p[0] = p[1] - p[3]
            elif p[2] == '*':
                p[0] = p[1] * p[3]
            elif p[2] == '/':
                p[0] = p[1] / p[3]
    else:
        p[0] = p[1]


def p_expr_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = -p[2]


def p_conditional(p):
    """conditional : IF condition
                   | IF statement
                   | IF statement ELSE statement
                   | WHILE condition
                   | WHILE statement
                   | Do statement WHILE condition"""
    if p[1].lower() == 'if' and len(p) == 3:
        p[0] = ('if', p[2], None)
    elif p[1].lower() == 'if' and len(p) == 5:
        p[0] = ('if-else', p[2], p[4])
    elif p[1].lower() == 'while' and len(p) == 3:
        p[0] = ('while', p[2], None)
    elif p[1].lower() == 'while' and len(p) == 4:
        p[0] = ('while', p[2], p[3])
    elif p[1].lower() == 'do' and len(p) == 5:
        p[0] = ('do-while', p[2], p[4])


def p_condition(p):
    """condition : TRUE
                 | FALSE"""
    p[0] = p[1]


def p_function_call(p):
    """function_call : IDENTIFIER '(' ')'
                     | IDENTIFIER '(' INT ')'
                     | IDENTIFIER '(' FLOAT ')'
                     | IDENTIFIER '(' BOOL ')'
                     | IDENTIFIER '(' STRING ')'
                     | IDENTIFIER '(' CHAR ')'"""
    if len(p) == 4:
        p[0] = ('function_call', p[1], None)
    else:
        p[0] = ('function_call', p[1], p[3])


# Error handling
def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

# Test the parser with a list of tokens
result = parser.parse(tokens)
print(result)
