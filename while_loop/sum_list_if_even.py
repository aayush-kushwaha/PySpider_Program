# # WAP to find the sum of values present in a given list only if the values are even
k = [5,6,7,8,9,10]
i = 0
out = 0
while i < len(k):
    if k[i] % 2 == 0:
        out = out + k[i]
    i = i + 1  
print(out)
# out = 0
# i = 0
# while i < len(k) and k[i] % 2 == 0:
#     out = out + k[i]
#     i = i + 1
# i = i + 1
# print(out)