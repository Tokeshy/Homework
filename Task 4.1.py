### Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.

def Replacer (in_str):
    out_str = ''
    for ch in in_str:
        if ch == '"' :
            ch = "'"
        elif ch == "'":
            ch = '"' 
        out_str = out_str + ch
    return out_str

inp_str = input()
print(Replacer(inp_str))