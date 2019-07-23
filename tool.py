import sys

def is_number(s):
    try:
        if float(s) or int(s) or int(s) == 0: 
            return True
    except ValueError:
        return False

def usage():
    print("python3 " + sys.argv[0] + " <option> <file>")
    print("options :")
    print("\tprint")
    print("\tinsert")
    print("\tupdate")


