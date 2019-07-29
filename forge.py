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
            lst = []
            for word in line.split('|'):
                if len(word) != 0:   
                    lst.append(word.strip())
                else:
                    lst.append("")
            l.append(lst)
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

    tot_len = col_max_len[1] + val_max_len[1]

    print("-" * (tot_len + 5))
    print("|" + str(table_name[:-1].center((tot_len + 3)) + "|"))
    print("|" + "-" * (tot_len + 3) + "|")

    for i in range(len(columns)):
        if columns[i] == "":
            continue;
        to_print = columns[i].ljust(col_max_len[1]) + " | " + values[i].rjust(val_max_len[1])
        print("|" + to_print + "|")
        print("|" + "-" * (col_max_len[1] + 1) + "+" + "-" * (val_max_len[1] + 1) + "|")
    exit()

def option(opt):
    dct = {
        "update": ["UPDATE", "SET"],
        "insert": ["INSERT INTO", "VALUES"]
    }
    return dct.get(opt)

query = option(sys.argv[2])
if query == None:
    usage()
    exit()

s = query[0] + " " + table_name
def forge(lst, query):

    if query == "INSERT" or query == "VALUES":
        s = " ("
        for i, elm in enumerate(lst):
            if elm.strip() == '' and (i == 0 or i == len(lst) - 1):
                continue
            if query != "VALUES" or is_number(elm) or elm == "NULL":
                s += elm.strip()
            else:
                s += "'" + elm.strip() + "'"
            s += ", "
        s = list(s)
        s[-2] = ")"

    elif query == "UPDATE":
        val = lst[1]
        s = " "
        for i, elm in enumerate(val):
            if elm.strip() == '' and (i == 0 or i == len(val) - 1):
                continue
            if is_number(elm) or elm == "NULL":
                s += lst[0][i] + "=" + elm.strip() + ", "
            else:
                s += lst[0][i] + "=" + "'" + elm.strip() + "'" + ", "
        s = list(s)
        s[-2] = ";"

    return "".join(s)

if query[0] == "INSERT INTO":
    s = s[:-1] + forge(columns, "INSERT") + query[1] + forge(values, "VALUES") + ";"
elif query[0] == "UPDATE":
    s = s[:-1] + " " + query[1] + forge(l, "UPDATE")
print(s)
