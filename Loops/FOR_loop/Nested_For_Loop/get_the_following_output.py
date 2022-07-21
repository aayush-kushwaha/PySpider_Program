'''
WAP to get the following output:
p = '33344563355644555'
out = '5'
'''
p = '33344563355644555'
out = '' # Taking dummy string to store the output here
count = 0 # Taking dummy count variable so that we can add +1 here when the condition gets satisfied.
for i in p: # Taking elements of p
    t = 0 # Taking t=0 inorder to compare with count and if it is greater than count then we will assign it as latest count
    for j in p: # Here also we are taking element of p so that we can check i == j by using relational operator.
        if i == j: # Here first i[0] will be compared with j[0,1,2,3,4,......,n]. And after the nested for loop terminates then it goes vack and then i[1] will be compared with j[0,1,2,3,4,......,n]
            t += 1 # Now if i will be equals to j then +1 will be added in this variable
    if t > count: # And the value of t(i.e also count) will be compared with count.. 
        count = t # if above condition satisfies then this will run and count will be assigned as 't' and it will have the latest value of count
        out = i # Here the element whose count is more will be taken. 
print(out) # Highest count element will be displayed here