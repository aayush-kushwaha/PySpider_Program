''' WAP to get the following output:
out = {'apple':2,'bananas':3,'mango':2,'grapes':2,'orange':3}
'''
v = ['apple','bananas','mango','grapes','orange']
out = {}
for i in v:
    count = 0 
    for j in i:
        if j in "aeiou":
            count += 1 # count = count + 1
    out[i] = count
print(out)
