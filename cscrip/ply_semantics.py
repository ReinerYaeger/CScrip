def __init__(self):
    self.variables = {}


def program_start(self, p):
    if isinstance(p[1], tuple):
        self.interpret_program(p[1])
    elif isinstance(p[1], tuple):
        self.interpret_statement(p[1])
    elif isinstance(p[1], list):
        self.interpret_data_structure(p[1])


def interpret_program(self, p):
    self.type_declaration = p[0]
    self.main_statement = p[1]
    if len(p) > 3 and p[2] == 'left_curl_op':
        self.inner_type_declaration = p[3]
        self.identifier = p[4]
        self.statement = p[7]
        self.right_curl_op = p[8]
    else:
        self.left_curl_op = p[2]
        self.statement = p[3]
        self.right_curl_op = p[4]
    pass


def interpret_statement(self, p):
    self.function_call_statement = p[0]
    self.conditional_statement = p[0]
    self.loop_statement = p[0]
    self.arithmetic_statement = p[0]
    self.break_statement = p[0]
    if p[0] == 'return_statement':
        self.return_statement = p[0][1]
    else:
        self.return_statement = p[0]


def interpret_function_call_statement(self, p):
    self.function_parameter = p[0]


def interpret_function_parameter(self, p):
    if len(p) == 1:
        self.literal = p[0]
        self.identifier = p[0]
        self.function_parameter_list = p[0]
    elif len(p) >= 3:
        self.left_curl_op = p[0]
        self.function_parameter = p[1]
        self.right_curl_op = p[2]
    pass


def interpret_conditional_statement(self, p):
    self.if_block == p[0]
    if len(p) == 1:
        self.if_block = p[0]
        self.else_block = p[1]
    elif len(p) >= 2:
        self.left_par_op = p[0]
        self.inequalities = p[1]
        self.right_par_op = p[2]
