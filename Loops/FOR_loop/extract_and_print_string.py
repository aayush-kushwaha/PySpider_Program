#WAP to extract(print in same line) all the uppercase characters present in a given string.
s = 'pRogRAMmInG'
st = ''
for i in s:
    if 'A' <= i <= 'Z':
        st = st + i
print(st)                       