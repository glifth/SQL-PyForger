from tool import *

#tuple for (position, len)
def fill_tuple(elm):
    tup = (0,0)
    for i, e in enumerate(elm):
        if len(e) > tup[1]:
            tup = (i, len(e))
    return tup

def prettyprint(columns, values, table_name):
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

def forge_insert(lst):
    s = ""
    for n ,l in enumerate(lst):
        s += " ("
        for i, elm in enumerate(l):
            if elm.strip() == '' and (i == 0 or i == len(l) - 1):
                continue
            if n == 0 or is_number(elm) or elm == "NULL":
                s += elm.strip()
            else:
                s += "'" + elm.strip() + "'"
            s += ", "
        s = list(s)
        s[-2] = ")"
        s = "".join(s)
        if n == 0:
            s += "VALUES"
        else:
            s += ";"
    return s

def forge_update(lst):
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
