import ply.lex as lex

reserved = {
    'if': 'if_statement',
    'else': 'else_statement',
    'elif': 'elif_statement',
    'while': 'while_statement',
    'do': 'do_statement',
    'for': 'for_statement',
    'int': 'int_declaration',
    'float': 'float_declaration',
    'double': 'double_declaration',
    'string': 'string_declaration',
    'char': 'char_declaration',
    'break': 'break_statement',
    'return': 'return_statement',
    'bool': 'bool_declaration',
    'Class': 'class',
    'struct': 'struct',
    'main': 'main_statement',
    'goto': 'goto_statement',
    'True': 'true_literal',
    'False': 'false_literal',
    'in': 'in_statement',
    'print': 'print_statement'
}

# List of token names
tokens = [
             'assign_op',
             'equivalent_op',
             'add_op',
             'sub_op',
             'not_equal',
             'and',
             'or',
             'mul_op',
             'expo_op',
             'div_op',
             'left_par_op',
             'right_par_op',
             'left_curl_op',
             'right_curl_op',
             'left_square_op',
             'right_square_op',
             'full_stop_statement',
             'comma_statement',
             'colon_statement',
             'semi_colon_statement',
             'single_quotes',
             'less_op',
             'great_op',
             'less_or_eq_op',
             'great_or_eq_op',
             'double_quotes',
             'float_literal',
             'int_literal',
             'double_literal',
             'string_literal',
             'bool_literal',
             'question_op',
             'list',
             'array',
             'char_literal',
             'increment',
             'decrement',
             'identifier',

         ] + list(reserved.values())

# Regular expression rules for simple tokens

t_class = r'class'
# t_struct = r'struct'
t_list = 'list'
t_array = 'array'
t_increment = r'\+\+'
t_decrement = r'--'
t_equivalent_op = r'=='
t_assign_op = r'='
t_print_statement = r'print'
t_add_op = r'\+'
t_sub_op = r'-'
t_expo_op = r'\*\*'
t_mul_op = r'\*'
t_div_op = r'/'
t_less_or_eq_op = r'<='
t_great_or_eq_op = r'>='
t_and = r'\&\&'
t_or = r'\|\|'
t_less_op = r'<'
t_great_op = r'>'
t_left_par_op = r'\('
t_right_par_op = r'\)'
t_left_curl_op = r'\{'
t_right_curl_op = r'\}'
t_left_square_op = r'\['
t_right_square_op = r'\]'
t_question_op = r'\?'
t_not_equal = r'!='
t_if_statement = r'if'
t_elif_statement = r'elif'
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
t_double_quotes = r'"'
t_int_declaration = r'int'
t_float_declaration = r'float'
t_double_declaration = r'double'
t_string_declaration = r'string'
t_char_declaration = r'char'
t_float_literal = r'(\.\d+)?.\d+f'
t_double_literal = r'\d+\.\d+'
t_string_literal = r'\'[^\']*\'|\"[^\"]*\"'
t_char_literal = r'[\'a-zA-Z\']'
t_identifier = r'[a-zA-Z_][a-zA-Z_\d+]*'


def t_int_literal(t):
    r'\d+'
    t.value = int(t.value)  # Convert the token value to an integer
    return t


def t_reserved(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'identifier')
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)  # Skip the illegal character

# lexer = lex.lex()
# content = ""

# with open('test/test.lang', 'r') as file:
#     content = file.read()
#     lexer.input(content)
#
#     for token in lexer:
#         print(token)
