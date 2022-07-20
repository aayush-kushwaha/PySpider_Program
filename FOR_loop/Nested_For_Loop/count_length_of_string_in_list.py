# WAP to count the length of string values present in a given list collection without using len() function.
v = ['apple','bananas','mango','grapes','orange']
count = 0
for i in v:
    for j in i:
        count += 1 #count = count + 1 
    print(count)
    count = 0 