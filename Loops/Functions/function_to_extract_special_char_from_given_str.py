'''
Define a function to extract all the special characters in the given string
'''
# Type-01 Function(Function with args and without return)
def special_char_extractor():
    a = input("Enter Character/String: ")
    out = ''
    for i in a:
        if not("A" <= i <= "Z" or "a" <= i <= "z" or "0" <= i <= "9"):
            out += i
    print(out)
special_char_extractor()