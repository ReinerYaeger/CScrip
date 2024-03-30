def main():
    # Read current source code in test.lang
    content = ""
    with open('test/test.lang', 'r') as file:
        content = file.read()

    # Lexer
    # Call the lexical and initialize it with the source code
    # lex = ply_lexer.t_STRING_DECLARATION(content)  # Pass the content as the source_code argument
    # tokens = lex.input()


if __name__ == "__main__":
    main()
