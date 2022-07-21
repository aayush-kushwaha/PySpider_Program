# WAP to print smallest divisor of a given number:
# n = 8
n = 8
for i in range(2,n+1): # Taking range from 2 to n+1 (i.e. 8+1)
    if n % i == 0: # Checking whether n is divisible by i or not
        print(i) # printing i
        break # Using break keyword to terminate the loop when the first condition (i.e. when the smallest divisor is found out.)
    