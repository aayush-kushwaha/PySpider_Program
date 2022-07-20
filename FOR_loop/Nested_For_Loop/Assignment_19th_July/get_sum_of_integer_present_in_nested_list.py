'''
WAP to get the sum of integers present in a nested list value in a given collection.
k = [4.5,3.5,[10,20],5,[1,2,[3,4]],4.5]
'''
k = [4.5,3.5,[10,20],5,[1,2,[3,4]],4.5]
# Python program to find sum of elements in list
total = 0
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(k)):
    total = total + k[ele]
# printing total value
print("Sum of all elements in given list: ", total)