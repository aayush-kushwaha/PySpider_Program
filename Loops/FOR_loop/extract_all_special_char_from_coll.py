# WAP to extract all the special characters present in a given string.
p = 'BTM_PySpiders$@#'
out = ""
for i in p:
    if not ("A" <= i <= "Z" or "a" <= i <= "z" or "0" <= i <= "9"):
        out = out + i
print(out)