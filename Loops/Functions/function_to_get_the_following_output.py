'''
Define a function to get the following output
a = "ISAFEAMSAFEASAFEGENIUS"
output = "I AM A GENIUS"
'''
# Type-01 Function(Function with args and without return)
def op_printer():
    out = ''
    a = "ISAFEAMSAFEASAFEGENIUS"
    b = a.split('SAFE') # b ---> ['I','AM','A','GENIUS']
    for i in b:
        out += i + ' '
    print(out)
    
op_printer()