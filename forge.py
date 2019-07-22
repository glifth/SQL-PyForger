import sys
from tool import *

l = []

pretty_print = 0

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
values  = l[1]

if sys.argv[2] == "print":
    #tuple for (position, len)
    def fill_tuple(elm):
        tup = (0,0)
        for i, e in enumerate(elm):
            if len(e) > tup[1]:
                tup = (i, len(e))
        return tup

    col_max_len = fill_tuple(columns)
    val_max_len = fill_tuple(values)

    print("-" * (col_max_len[1] + val_max_len[1] + 5))
    print("|" + str(table_name[:-1].center((col_max_len[1] + val_max_len[1] + 3)) + "|"))
    print("|" + "-" * (col_max_len[1] + val_max_len[1] + 3) + "|")

    for i in range(len(columns)):
        to_print = columns[i].ljust(col_max_len[1]) + " | " + values[i].rjust(val_max_len[1])
        print("|" + to_print + "|")
        print("|" + "-" * (int(len(to_print)/2) + 1) + "+" + "-" * (int(len(to_print)/2) - 1) + "|")
    exit()

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
    return "".join(s)

s = s[:-1] + fill_parenthesis(columns) + query[1] + fill_parenthesis(values, 1) + ";"

print(s)
