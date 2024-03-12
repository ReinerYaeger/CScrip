

Grammar
Derivation
Program_start – Type_Declaration | main_statement | left_curl_op | Statement | right_curl_op | Function_Declaration | Structure

Structure - Class | Struct

Class - class_statment Identifer left_curl_op Statement right_curl_op

Statement –Function_Call_Statement, Conditional_Statement,  Loop_Statement, Arithmetic_Op,Arithmetic_statement,arithmetbreak_statement

Function_call_statement – Identifer  (Identifer | Type_Literal | comma_statement
 Identifer | comma_statement  Type_Declaration)*

Function_Declaration - Type_Declaration Identifer (Type_Declaration Identifer | comma_statement Type_Declaration Identifer)* left_curl_op
                        Statement return_statement (Identifer|Type_Literal) right_curl_op

Conditional_Statement – If_statement Control_Structure_Input left_curl_op Statement right_curl_op

Control_Structure_Input - ((Identifer) | (Type_Literal) | (Identifer Inequalities (Identifer| Type_Literal)))


Arithmetic_statement - (left_par_op Arithmetic_statement right_par_op) | (Type_Literal|Identifer) (Arithmetic_Op) (Type_Literal|Identifer) |

Loop_Statement – (while_statement  Control_Structure_Input left_curl_op Statement right_curl_op) |
                 (do_statement left_curl_op Statement right_curl_op while_statement Control_Structure_Input) |
                 for_statement ((Type_Declaration Identifier assign_op (Identifer | Type_Literal)) | (Type_Literal |  Identifer ))? semi_colon_statement
                 ((Identifer | Type_Literal) Inequalities (Identifer | Type_Literal))? semi_colon_statement
                 (Identifer Arithmetic_Op (Identifer|Type_Literal)left_curl_op) Statement right_curl_op


Arithmetic_Op - add_op | sub_op | mul_op | div_op
Inequalities - less_op | great_op | less_or_eq_op | great_or_eq_op | equivalent_op

Type_Declaration – int_declaration | float_declaration | string_declaration | double_declaration | char_declaration | Boolean Declaration
Type_Literal - int_literal | float_literal | double_literal | char_literal | bool_literal | string_literal



Program_start ::= Type_Declaration | main_statement | left_curl_op | Statement | right_curl_op | Function_Declaration

Statement ::= Function_Call_Statement | Conditional_Statement | Loop_Statement | Arithmetic_Op | Arithmetic_statement | arithmetbreak_statement

Function_Call_Statement ::= Identifier  (Identifier | Type_Literal | comma_statement Identifier | comma_statement  Type_Declaration)*

Function_Declaration ::= Type_Declaration Identifier (Type_Declaration Identifier | comma_statement Type_Declaration Identifier)* left_curl_op
                        Statement return_statement (Identifier | Type_Literal) right_curl_op

Conditional_Statement ::= If_statement Control_Structure_Input left_curl_op Statement right_curl_op

Control_Structure_Input ::= (Identifier) | (Type_Literal) | (Identifier Inequalities (Identifier | Type_Literal))

Arithmetic_statement ::= (left_par_op Arithmetic_statement right_par_op) | (Type_Literal | Identifier) (Arithmetic_Op) (Type_Literal | Identifier) |

Loop_Statement ::= (while_statement Control_Structure_Input left_curl_op Statement right_curl_op) |
                  (do_statement left_curl_op Statement right_curl_op while_statement Control_Structure_Input) |
                  for_statement ((Type_Declaration Identifier assign_op (Identifier | Type_Literal)) | (Type_Literal | Identifier ))? semi_colon_statement
                  ((Identifier | Type_Literal) Inequalities (Identifier | Type_Literal))? semi_colon_statement
                  (Identifier Arithmetic_Op (Identifier | Type_Literal) left_curl_op) Statement right_curl_op

Arithmetic_Op ::= add_op | sub_op | mul_op | div_op
Inequalities ::= less_op | great_op | less_or_eq_op | great_or_eq_op | equivalent_op

Type_Declaration ::= int_declaration | float_declaration | string_declaration | double_declaration | char_declaration | Boolean Declaration
Type_Literal ::= int_literal | float_literal | double_literal | char_literal | bool_literal | string_literal
