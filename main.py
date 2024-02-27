import lexcial  # Assuming you have the 'lexical' module imported correctly


def main():
    # Read current source code in test.lang
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()

    # Lexer
    # Call the lexical and initialize it with the source code
    lex = lexcial.Lexer(content)  # Pass the content as the source_code argument
    tokens = lex.tokenize()


if __name__ == "__main__":
    main()
