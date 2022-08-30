import copy
#stock of tex command(to write by python)
newline = r" \\ "
hline = r" \hline"
div = " & "
doc_i = r"\begin{document}" +"\n"
doc_f = r"\end{document}" + "\n"
table_package = r"""\documentclass[10pt]{article}
\usepackage[usenames]{color} %フォントカラー
\usepackage{amssymb} %数式記号
\usepackage{amsmath} %数式
\usepackage[utf8]{inputenc} %発音区別符アルファベットの直接入力
\usepackage{braket}
\usepackage{setspace}
\usepackage{multirow}
\usepackage{multicol}
\usepackage{float}

"""
def ftable_i_simple(caption,colop,*cols):
    table_i  = r"\begin{table}[H]"+"\n"
    table_i += r" \caption{"+caption+"}\n"
    table_i += r"  \begin{tabular}{"+colop+"}\hline \hline"+"\n"
    for col in cols:
        table_i += div + col
    table_i += r" \\ \hline"+"\n"
    return table_i

def ftable_i(caption,colop):
    table_i  = r"\begin{table}[H]"+"\n"
    table_i += r" \caption{"+caption+"}\n"
    table_i += r"  \begin{tabular}{"+colop+"}\hline \hline"+"\n"
    return table_i

def fbodyline(val_list,col1=""):
    body = "" +col1
    for elm in val_list:
        body += div + elm
    body +=newline +"\n"
    return body

def ftable_f(labelname):
    table_f = r"  \end{tabular}" +"\n"
    table_f += r" \label{tab:"+labelname +"}\n"
    table_f += r"\end{table}"+"\n"
    return table_f
