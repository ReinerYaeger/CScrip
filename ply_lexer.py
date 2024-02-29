import ply.lex as lex

# --- Tokenizer

# All tokens must be named in advance.
tokens = (
    'IDENTIFIER', 'EQUAL_OP', 'EQUIVALENT_OP', 'ADD_OP', 'POSITIVE_OP', 'NEGATIVE_OP', 'SUB_OP', 'MUL_OP', 'DIV_OP',
    'LEFT_PAR_OP', 'RIGHT_PAR_OP', 'IF_STATEMENT', 'ELSE_STATEMENT', 'WHILE_STATEMENT', 'FOR_STATEMENT', 'LEFT_CURL_OP',
    'RIGHT_CURL_OP', 'FULL_STOP_STATEMENT', 'IF_STATEMENT', 'ELSE_STATEMENT', 'COLON_STATEMENT', 'SEMI_COLON_STATEMENT',
    'INT_DECLARATION', 'FLOAT_DECLARATION', 'DOUBLE_DECLARATION', 'STRING_DECLARATION', 'CHARACTER_DECLARATION',
    'BOOL_STATEMENT', 'VOID_STATEMENT', 'CLASS_STATEMENT', 'OBJECT_STATEMENT', 'STRUCT_STATEMENT', 'DO_STATEMENT')

# Ignored characters
t_ignore = ' \t'

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
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
t_COLON_STATEMENT = r':'
t_SEMI_COLON_STATEMENT = r';'
t_INT_DECLARATION = r'int'
t_FLOAT_DECLARATION = r'float'
t_DOUBLE_DECLARATION = r'double'
t_STRING_DECLARATION = r'string'
t_CHARACTER_DECLARATION = r'char'
t_BOOL_STATEMENT = r'bool'
t_VOID_STATEMENT = r'void'
t_CLASS_STATEMENT = r'class'
t_OBJECT_STATEMENT = r'object'
t_STRUCT_STATEMENT = r'struct'
t_DO_STATEMENT = r'do'
t_IF_STATEMENT = r'if'
t_ELSE_STATEMENT = r'else'
t_WHILE_STATEMENT = r'while'
t_FOR_STATEMENT = r'for'
t_SINGLE_QUOTES = r'\''
t_DOUBLE_QUOTES = r'\"'
t_INT_LITERAL = r'\d+'
t_ELSEIF_STATEMENT = r'elseif'


# A function can be used if there is an associated action.
# Write the matching regex in the docstring.

def t_INT_DECLARATION(t):
    """Recognize integer declarations and convert them to integers."""
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT_DECLARATION(t):
    """Recognize Float declarations and convert them to Float."""
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_STRING_DECLARATION(t):
    """Recognize strings enclosed in double quotes."""
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove quotes
    return t


# Define a rule for characters
def t_CHARACTER_DECLARATION(t):
    """Recognize characters enclosed in single quotes."""
    r"'.'"
    t.value = t.value[1]  # Remove quotes
    return t


def t_BOOL_STATEMENT(t):
    """Recognize characters enclosed in single quotes."""
    r'True|False'
    t.value = t.value == 'True'
    return t


def t_CLASS_STATEMENT(t):
    """Recognize statement that start with class."""
    r'class'
    return t


def t_VOID_STATEMENT(t):
    """Recognize statement that has void in it."""
    r'void'
    return t


def t_IF_STATEMENT(t):
    """Recognize if statements."""
    r'(IF|if)'
    return t


def t_FULL_STATEMENT(t):
    """Recognize Full stop statements."""
    r'.'
    return t


def t_ELSE_STATEMENT(t):
    """Recognize else statements."""
    r'(ELSE|else)'
    return t


def t_WHILE_STATEMENT(t):
    """Recognize while statements."""
    r'(WHILE|while)'
    return t


def t_DO_STATEMENT(t):
    """Recognize Do statements."""
    r'(DO|do)'
    return t


def t_FOR_STATEMENT(t):
    """Recognize For statements."""
    r'(FOR|for)'
    return t


def t_STRUCT_STATEMENT(t):
    """Recognize Struct statements."""
    r'Struct'
    return t


def t_OBJECT_STATEMENT(t):
    """Recognize Object statements."""
    r'Object'
    return t


# Ignored token with an action associated with it
def t_ignore_newline(t):
    """Recognize newline numbers."""
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
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
