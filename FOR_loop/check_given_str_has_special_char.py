# WAP to check whether the given string is having a special character or not.
p = 'BTM_PySpiders'
for i in p:
    if not("A" <= i <= "Z" or "a" <= i <= "z" or "0" <= i <= "9"): #Always use double quotes while checking the values
        print(i)