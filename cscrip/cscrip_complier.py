import ply.yacc as yacc

from .lex import *
from .py_parser import *
from .ply_semantics import semantic_node


def compiler(input_code="x=1"):

    lexer = lex.lex()
    content = ""

        # Build the parser
    parser = yacc.yacc()



    lexer.input(input_code)
    for token in lexer:
        print(token)

    parsed_expression = parser.parse(input_code)
    print("Parsed expression:", parsed_expression)

    # Pass the root node of the parse tree to the semantic analysis function
    ast = semantic_node(parsed_expression, symbol_table)
    print("Interpreter result:", ast)
    return ast