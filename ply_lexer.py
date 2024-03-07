import ply.lex as lex

reserved = {
    'if': 'IF_STATEMENT',
    'then': 'THEN_STATEMENT',
    'else': 'ELSE_STATEMENT',
    'while': 'WHILE_STATEMENT',
    'for': 'FOR_STATEMENT',
    'class': 'CLASS_STATEMENT',
    'struct': 'STRUCT_STATEMENT',
    'object': 'OBJECT_STATEMENT',
    'void': 'VOID_STATEMENT',
    'bool': 'BOOL_STATEMENT',
    'elseif': 'ELSEIF_STATEMENT',
    'string': 'STRING_STATEMENT',
    'int': 'INT_STATEMENT',
    'float': 'FLOAT_STATEMENT',
    'double': 'DOUBLE_STATEMENT',
    'char': 'CHARACTER_STATEMENT',
    'true': 'TRUE_STATEMENT',
    'false': 'FALSE_STATEMENT',
    'do': 'DO_STATEMENT',
    'print': 'PRINT_STATEMENT'
}

# --- Tokenizer

# All tokens must be named in advance.
tokens = ([
              'EQUAL_OP', 'EQUIVALENT_OP', 'ADD_OP', 'POSITIVE_OP', 'NEGATIVE_OP',
              'SUB_OP', 'MUL_OP', 'DIV_OP', 'LEFT_PAR_OP', 'RIGHT_PAR_OP', 'LEFT_CURL_OP', 'RIGHT_CURL_OP',
              'FULL_STOP_STATEMENT', 'COLON_STATEMENT', 'SEMI_COLON_STATEMENT',
              'INT_DECLARATION', 'FLOAT_DECLARATION', 'DOUBLE_DECLARATION', 'STRING_DECLARATION',
              'CHARACTER_DECLARATION', 'SINGLE_QUOTES', 'DOUBLE_QUOTES', 'INT_LITERAL',
              'IDENTIFIER'] + list(reserved.values()))

# Ignored characters
t_EQUAL_OP = r'='
t_EQUIVALENT_OP = r'=='
t_ADD_OP = r'\+\+'
t_POSITIVE_OP = r'\+'
t_SUB_OP = r'-'
t_NEGATIVE_OP = r'\-'
t_MUL_OP = r'\*'
t_DIV_OP = r'/'
t_LEFT_PAR_OP = r'\('
t_RIGHT_PAR_OP = r'\)'
t_RIGHT_CURL_OP = r'\{'
t_LEFT_CURL_OP = r'\}'
t_FULL_STOP_STATEMENT = r'\.'
t_COLON_STATEMENT = r'\:'
t_SEMI_COLON_STATEMENT = r';'
t_SINGLE_QUOTES = r'\''
t_DOUBLE_QUOTES = r'\"'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.

t_ignore = ' \t\n!'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t


def t_INT_LITERAL(t):
    """Recognize integer declarations and convert them to integers."""
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT_LITERAL(t):
    """Recognize Float declarations and convert them to Float."""
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_eof(t):
    more = input('...')
    if more:
        lexer.input(more)
        return lexer.token()  # Return a single token
    return None  # Return None to indicate end of input


# Ignored token with an action associated with it
def t_newline(t):
    """Recognize newline numbers."""
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handler for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Define your token types and lexer rules here

# Build the lexer
lexer = lex.lex()
# Now you can use the lexer object to tokenize input
with open('test.lang', 'r') as file:
    content = file.read()
lexer.input(content)

# Iterate over the tokens produced by the lexer
for tok in lexer:
    print(tok)

# # --- Parser
#
# # Write functions for each grammar rule which is
# # specified in the docstring.
# def p_expression(p):
#     '''
#     expression : term PLUS term
#                | term MINUS term
#     '''
#     # p is a sequence that represents rule contents.
#     #
#     # expression : term PLUS term
#     #   p[0]     : p[1] p[2] p[3]
#     #
#     p[0] = ('binop', p[2], p[1], p[3])
#
#
# def p_expression_term(p):
#     '''
#     expression : term
#     '''
#     p[0] = p[1]
#
#
# def p_term(p):
#     '''
#     term : factor TIMES factor
#          | factor DIVIDE factor
#     '''
#     p[0] = ('binop', p[2], p[1], p[3])
#
#
# def p_term_factor(p):
#     '''
#     term : factor
#     '''
#     p[0] = p[1]
#
#
# def p_factor_number(p):
#     '''
#     factor : NUMBER
#     '''
#     p[0] = ('number', p[1])
#
#
# def p_factor_name(p):
#     '''
#     factor : NAME
#     '''
#     p[0] = ('name', p[1])
#
#
# def p_factor_unary(p):
#     '''
#     factor : PLUS factor
#            | MINUS factor
#     '''
#     p[0] = ('unary', p[1], p[2])
#
#
# def p_factor_grouped(p):
#     '''
#     factor : LPAREN expression RPAREN
#     '''
#     p[0] = ('grouped', p[2])
#
#
# def p_error(p):
#     print(f'Syntax error at {p.value!r}')
#
#
# # Build the parser
# parser = yacc()
#
# # Parse an expression
# ast = parser.parse('2 * 3 + 4 * (5 - x)')
# print(ast)
