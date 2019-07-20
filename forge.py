import sys
from tool import *

l = []

if len(sys.argv) != 3:
    usage()
    exit()

with open(sys.argv[1]) as file:
    i=1
    for i, line in enumerate(file):
        if i == 0:
            table_name = line
        else:
            l.append( [word for word in line.replace("|"," ").split()] )

columns = l[0]
values = l[1]

def option(opt):
    dct = {
        "update": ["UPDATE", "VALUES"],
        "insert": ["INSERT INTO", "VALUES"],
    }
    return dct.get(opt)

query = option(sys.argv[2])
if query == None:
    usage()
    exit()

s = query[0] + " " + table_name

def fill_parenthesis(lst, n=0):
    s = " ("
    for i, elm in enumerate(lst):
        if elm.strip() == '' and (i == 0 or i == len(lst) - 1):
            continue
        if n == 0 or is_number(elm) or elm == "NULL":
            s += elm.strip()
        else:
            s += "'" + elm.strip() + "'"
        s += ", "
    s = list(s)
    s[-2] = ")"

s = s[:-1] + fill_parenthesis(columns) + query[1] + fill_parenthesis(values, 1) + ";"
print(s)
