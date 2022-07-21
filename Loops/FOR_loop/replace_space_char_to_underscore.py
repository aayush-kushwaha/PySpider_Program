# WAP to replace all the space characters to underscore characters in given string.
p = ('East or West Python is the best')
out = ""
for i in p:
    if i == " ":
        out += "_" # out = out + "_"
    else:
        out += i # out = out + i
print(out)