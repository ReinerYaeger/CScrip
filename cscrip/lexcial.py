import re


class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        # All tokens are stored here
        tokens = []

        # Create a list of the source code
        source_code = self.source_code.split()

        # Helps keeps track of the word index in the source code
        source_code_index = 0

        # Generate tokens in the source code by looping through the code
        while source_code_index < len(source_code):
            word = source_code[source_code_index]
            if word == "int":
                tokens.append(["int_declaration", word])
            elif word == "float":
                tokens.append(["float_declaration", word])
            elif word == "double":
                tokens.append(["double_declaration", word])
            elif word == "string":
                tokens.append(["string_declaration", word])
            elif word == "char":
                tokens.append(["character_declaration", word])
            elif word == "=":
                tokens.append(["equal_op", word])
            elif word == "+":
                tokens.append(["add_op", word])
            elif word == "-":
                tokens.append(["sub_op", word])
            elif word == "*":
                tokens.append(["mul_op", word])
            elif word[len(word) - 1] == "(":
                tokens.append(["left_par_op", word[-1]])
            elif word[len(word) - 1] == ")":
                tokens.append(["right_par_op", word[-1]])
            elif word[len(word) - 1] == "{":
                tokens.append(["left_curl_op", word[-1]])
            elif word[len(word) - 1] == "}":
                tokens.append(["right_curl_op", word[-1]])
            elif word == "if":
                tokens.append(["if_statement", word])
            elif word == "else":
                tokens.append(["else_statement", word])
            elif word == "while":
                tokens.append(["while_statement", word])
            elif word == "for":
                tokens.append(["for_statement", word])
            elif word == "do":
                tokens.append(["do_statement", word])
            elif word[len(word) - 1] == ".":
                tokens.append(["full_stop_statement", word[-1]])
            elif word == ":":
                tokens.append(["colon_statement", word])
            elif word[len(word) - 1] == ";":
                tokens.append(["semi_colon_statement", word[-1]])
            elif re.match("'", word[len(word) - 1]) or re.match("'", word[len(word) - 1]):
                tokens.append(['single_quote', word[-1]])
            elif re.match('"', word[len(word) - 1]) or re.match('"', word[len(word) - 1]):
                tokens.append(['double_quote', word[-1]])
            elif word == 'elseif':
                tokens.append(["elseif_statement", word])
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                tokens.append(['identifier', word])
            elif re.match('[0-9]', word):
                tokens.append(['integer', word])

            # Increase the word index after checking it
            source_code_index += 1

            print(tokens)
        # Return created tokens
        return tokens

    # Define t_ignore inside the class
    t_ignore = '\t\n'
