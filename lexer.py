import ply.lex as lex

# ... (تعريف الرموز المميزة والكلمات المفتاحية)

def t_COMMENT(t):
    r'\#.*'
    pass

# ... (تعريف بقية الرموز)

lexer = lex.lex()
