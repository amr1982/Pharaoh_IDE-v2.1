import ply.yacc as yacc
from lexer import tokens
from memory import set_variable, get_variable

# ... (قواعد النحو)

parser = yacc.yacc()
