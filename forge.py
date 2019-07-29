import sys
from tool import *
from options import *

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
    prettyprint(columns, values, table_name)
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

if query[0] == "INSERT INTO":
    s = s[:-1] + forge_insert(l)

elif query[0] == "UPDATE":
    s = s[:-1] + " " + query[1] + forge_update(l)
print(s)
