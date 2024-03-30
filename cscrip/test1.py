import ply.lex as lex

# List of reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR'
}

# List of token names
tokens = [
             'NUMBER',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'EQUALS',
             'LPAREN',
             'RPAREN',
             'ID'
         ] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Define a rule for IDs (identifiers and reserved words)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Define a rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule for ignoring whitespace
t_ignore = ' \t'


# Define a rule for tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test the lexer
data = '''
if x == 0:
    y = 2 * x + 1
else:
    y = 3 * x - 1
'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
