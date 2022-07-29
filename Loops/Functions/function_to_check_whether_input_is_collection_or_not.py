'''
Define a function to check whether the given input is a collection or not.
'''
# Type-01 Function(Function with args and without return)
def coll_check():
    a = input("Enter Character/String: ")
    if type(a) in [str,list,tuple,set,dict]:
        print("Collection!")
    else:
        print("Not a collection!")
coll_check()