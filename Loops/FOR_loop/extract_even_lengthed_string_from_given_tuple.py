# WAP to extract all the even lengthed string present in a given tuple
p = ('python','Btm_layout','bengaluru','pyspiders','july')
out = ()
for i in p:
    if len(i) % 2 == 0:
        out += (i,) # It is a way to concatenate with tuple
print(out)