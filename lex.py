import ply.lex as lex

# List of token names
tokens = [
    'identifier',
    'assign_op',
    'equivalent_op',
    'add_op',
    'sub_op',
    'mul_op',
    'Expo_op',
    'div_op',
    'left_par_op',
    'right_par_op',
    'left_curl_op',
    'right_curl_op',
    'if_statement',
    'else_statement',
    'while_statement',
    'for_statement',
    'do_statement',
    'Break_statement',
    'Return_statement',
    'full_stop_statement',
    'comma_statement',
    'colon_statement',
    'semi_colon_statement',
    'single_quotes',
    'Less_op',
    'Great_op',
    'Less_or_eq_op',
    'Great_or_eq_op',
    'double_quotes',
    'int_declaration',
    'float_declaration',
    'double_declaration',
    'string_declaration',
    'int_literal',
    'float_literal',
    'double_literal',
    'string_literal',
    'char_literal',
    'bool_literal',
    'class',
    'struct',
]

# Regular expression rules for simple tokens
t_class_statement = r'class'
t_struct_statement = r'struct'
t_assign_op = r'='
t_equivalent_op = r'=='
t_add_op = r'\+'
t_sub_op = r'-'
t_mul_op = r'\*'
t_expo_op = r'\*\*'
t_div_op = r'/'
t_left_par_op = r'\('
t_right_par_op = r'\)'
t_left_curl_op = r'\{'
t_right_curl_op = r'\}'
t_if_statement = r'if'
t_else_statement = r'else'
t_while_statement = r'while'
t_for_statement = r'for'
t_do_statement = r'do'
t_break_statement = r'break'
t_return_statement = r'return'
t_full_stop_statement = r'\.'
t_comma_statement = r','
t_colon_statement = r':'
t_semi_colon_statement = r';'
t_single_quotes = r'\''
t_less_op = r'<'
t_great_op = r'>'
t_less_or_eq_op = r'<='
t_great_or_eq_op = r'>='
t_double_quotes = r'"'
t_int_declaration = r'Int'
t_float_declaration = r'Float'
t_double_declaration = r'Double'
t_string_declaration = r'String'
t_int_literal = r'[0-9]'
t_float_literal = r'[0-9].[0-9]f'
t_double_literal = r'[0-9].[0-9]'
t_string_literal = r'\'[^\']*\'|\"[^\"]*\"'
t_char_literal = r'[a-zA-Z0-9]'
t_bool_literal = r'True|False'


# A regular expression rule with some action code
def t_identifier(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'identifier')
    return t

# Define a rule to ignore whitespace characters
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Reserved words
reserved = {
    'int': 'int_declaration',
    'float': 'float_declaration',
    'double': 'double_declaration',
    'string': 'string_declaration',
}

# Build the lexer
lexer = lex.lex()

# Test the lexer with an example input

# Build the lexer
lexer = lex.lex()
content = ""
# Now you can use the lexer object to tokenize input
with open('test/test.lang', 'r') as file:
    content = file.read()
    lexer.input(content)

# Iterate over the tokens produced by the lexer
    for token in lexer:
        print(token)



# Print the tokens
for token in lexer:
    print(token)
