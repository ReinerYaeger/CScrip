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

# All tokens must be named in advance.
tokens = [
             'EQUAL_OP', 'EQUIVALENT_OP', 'ADD_OP', 'SUB_OP', 'MUL_OP', 'DIV_OP',
             'LEFT_PAR_OP', 'RIGHT_PAR_OP', 'LEFT_CURL_OP', 'RIGHT_CURL_OP',
             'FULL_STOP_STATEMENT', 'COLON_STATEMENT', 'SEMI_COLON_STATEMENT',
             'MINUS', 'FLOAT_DECLARATION', 'DOUBLE_DECLARATION', 'STRING_DECLARATION',
             'CHARACTER_DECLARATION', 'SINGLE_QUOTES', 'DOUBLE_QUOTES', 'INT_LITERAL',
             'IDENTIFIER', 'ASSIGNMENT_STATEMENT', 'TERM', 'TYPE', 'EXPRESSION', 'NUMBER'
         ] + list(reserved.values())

# Regular expression rules for tokens
t_ignore = ' \t\n'
t_EQUAL_OP = r'='
t_EQUIVALENT_OP = r'=='
t_ADD_OP = r'\+'
t_SUB_OP = r'-'
t_MUL_OP = r'\*'
t_DIV_OP = r'/'
t_LEFT_PAR_OP = r'\('
t_RIGHT_PAR_OP = r'\)'
t_RIGHT_CURL_OP = r'\}'
t_LEFT_CURL_OP = r'\{'
t_FULL_STOP_STATEMENT = r'\.'
t_COLON_STATEMENT = r'\:'
t_SEMI_COLON_STATEMENT = r';'
t_SINGLE_QUOTES = r'\''
t_DOUBLE_QUOTES = r'\"'


# Define regular expressions for other tokens (IDENTIFIER, INT_LITERAL, etc.)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t


def t_EXPRESSION(t):
    r'\d+(\.\d+)?'  # Match integers and floats
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_INT_LITERAL(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t


def t_FLOAT_LITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


# Ignored token with an action associated with it
def t_newline(t):
    """Recognize newline numbers."""
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handler for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Now you can use the lexer object to tokenize input
with open('test.lang', 'r') as file:
    content = file.read()
    lexer.input(content)

# Iterate over the tokens produced by the lexer
for token in lexer:
    print(token)
