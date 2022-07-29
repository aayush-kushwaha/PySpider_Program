'''
WAP to count the number of values present in a collection without using len() function in the form of 
user-defined function.
'''
# Type-01 Function(Function with args and without return)
def value_counter():
    a = input("Enter character/string: ")
    count = 0
    for i in a:
        count += 1
    print(count)
value_counter()