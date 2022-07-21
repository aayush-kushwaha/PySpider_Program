#WAP to find the sum of integer value present only at even index in a given heterogeneous collection.
'''h = ['apple',1,4.5,3,4+5j,True,6,7,6.5]
sum_int = 0
for i in range(len(h)):
    if i % 2 == 0 and type(h[i]) == int:
        sum_int = sum_int + h[i]
print(sum_int)
'''
h = ['apple',1,4.5,3,4+5j,True,6,7,6.5]
sum_int = 0
for i in range(0,len(h)):
    if i % 2 == 0 and type(h[i]) == int:
        sum_int += h[i] #sum_int = sum_int + h[i]
print(sum_int)
