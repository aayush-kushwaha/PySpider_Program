# WAP to extract all the integers present at even index in a given collection using continue statements
k = ['python', 12.5, 4, 6+3j, 4, 7, 5, True, 10, 'nohtyp']
out = [] # Taking empty/dummy list so that we can store the elements here
for i in range(len(k)): # Taking range from 0 to len(k)
     if i % 2 == 0 and type(k[i]) == int: # Assigning conditions to check if it is an even index and if the type of element is integer or not
         out += [k[i]] # k[i] means we are taking index of loop. And concatenating the element if the above condition satisfies in out variable
     else:
         continue # Continue is a keyword which is used to skip the current execution and make the control to go for next next iteration
print(out) # Printing out




# Another method:
'''
for i in range(len(k)): # Taking range from 0 to len(k)
    if i % 2 != 0 or type(k[i]) != int: # Assigning conditions if it is not an even index and if the type of element is not integer then we will continue
        continue # Continue is a keyword which is used to skip the current execution and make the control to go for next next iteration
    else:
        out += [k[i]] # k[i] means we are taking index of loop. And concatenating the element if the above condition satisfies in out variable
print(out)
'''





