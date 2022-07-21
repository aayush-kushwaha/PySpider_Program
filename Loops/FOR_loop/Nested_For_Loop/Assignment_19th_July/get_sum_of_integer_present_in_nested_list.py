'''
WAP to get the sum of integers present in a nested list value in a given collection.
k = [4.5,3.5,[10,20],5,6,[1,2,[3,4]],4.5]
'''
k = [4.5,3.5,[10,20],5,6,[1,2,[3,4]],4.5]
out = 0
for i in k:
    if type(i) == list:
        for j in  i:
            if type(j) == int:
                out += j
            elif type(j) == list:
                for k in j:
                    if type(k) == int:
                        out += k
print(out)