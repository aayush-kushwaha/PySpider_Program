# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for i in numbers:
#         squared_numbers.append(i*i)
#     return squared_numbers
    

# numbers = [2,5,8,9]
# get_squared_numbers(numbers)
# print(get_squared_numbers(numbers))

#WAP to find duplicated from values from the collection (CODEBASIC Yt Question)
numbers = [3,6,2,4,3,6,8,9]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i],"is a duplicate")  