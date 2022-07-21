# WAP to check whether the given number is prime or not
# NOTE: Here we are not generating series of prime number. So we are using break.
n = 5
for i in range(2,n): # Taking range from 0 to n. Here n is 5 but the range will take upto 4.
    if n % i == 0: # If the number is divisibe by 2 to n, it will be not prime
        print("Not Prime") # Printing not prime
        break # Using break keyword to terminate the loop when the first condition is satisfied (i.e. when n % i == True)
else:
    print("Prime") #Otherwise We will print Prime