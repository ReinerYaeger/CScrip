import ply.yacc as yacc

from ply_parser import *
from ply_semantics import semantic_node


def cscrip():
    parsed_expression = parser.parse(lex)
    semantic_node(lex, symbol_table)
