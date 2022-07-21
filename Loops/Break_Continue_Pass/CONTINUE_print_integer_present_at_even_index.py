# WAP to extract all the integers present at even index in a given collection using continue statements
k = ['python', 12.5, 4, 6+3j, 4, 7, 5, True, 10, 'nohtyp']
out = []
for i in range(len(k)):
     if i % 2 == 0 and type(k[i]) == int:
         out += [k[i]]
     else:
         continue
print(out)




# Another method:
'''
for i in range(len(k)):
    if i % 2 != 0 or type(k[i]) != int:
        continue
    else:
        out += [k[i]]
print(out)
'''





