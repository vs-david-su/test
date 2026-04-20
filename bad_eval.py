# bad_eval.py
import ast

def process_data(user_input):
    # 這行會被我們剛才寫的 Semgrep 規則抓到
    result = eval(user_input)
    return result