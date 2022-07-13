a = input("Enter the string: ")
i = 0
while i < len(a):
    if a[i] in "aeiouAEIOU":
        print(a[i],"vowel")
    else:
        print(a[i],"consonant")
    i = i + 1