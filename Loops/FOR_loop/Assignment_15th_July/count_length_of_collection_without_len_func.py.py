# WAP to count the length of the collection without using len() function
l = [10,20,30,1,2,3,9,7,6]
count = 0
for i in l:
    length = count + 1
    count = length
print(count)
