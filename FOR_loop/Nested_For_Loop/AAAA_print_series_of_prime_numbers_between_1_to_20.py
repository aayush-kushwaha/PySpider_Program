# WAP to print the series of prime numbers between the range 1 to 20
for i in range(1,21):
    indicator = 0
    for j in (2,i):
        if i % j == 0:
            indicator = 1
        if indicator == 0:
            print(i)

# for i in range(1,21):
#     ind = 0
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 ind = 1
#             if ind == 0:
#                 print(i)    