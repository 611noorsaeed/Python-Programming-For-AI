# # 1 concatenation
#
# # str1 = "Noor"
# # str2 = "Saeed"
# #
# # name = str1 + " " + str2
# # print(name)
#
#
# # 2 repition = *
# # message = "Hi "
# # multiple_message = message * 4
# # print(multiple_message)
#
# # 3 len
# # a = "Noor Saeed"
# # print(len(a))
#
#
# # method
# # 1 upper() and lower()
# # a = "this is my string"
# # b = "THIS is MY STRing"
# # print(a.upper())
# # print(b.lower())
#
#
#
# # 2 capitalize
# # a = "this is your string. how are you"
# # print(a.capitalize())
#
# # 3 title()
# # a = 'this is my book'
# # print(a.title())
#
# # 4 strip()
# # a = "  Noor Saeed "
# # print(a)
# # print(a.strip())
#
# # 5 replace()
# # a = "Learn ML or DL"
# # print(a.replace('ML','Machine Learning'))
#
# # split()
# # a = "This is a book"
# # print(a.split())
#
# # 6 join()
# # a = ["helo",'world','Noor']
# # print(" ".join(a))
#
# # 7 find()
# # a = "this is my link https//:.com wow this is good"
# # print(a.find('https//:.com'))
#
# #8 count()
#
# # a = "Hello World"
# # print(a.count('o'))
#
# # 9 startswith() and endswith()
# # str1 = "Hello World"
# # print(str1.startswith("Hello"))  # Output: True
# # print(str1.endswith("World"))
#
#
# # 10 format() and f string
#
# a = 20
# b = 30
# print("a value is : {} and b value is {}".format(a,b))
#
# print(f"a value {a} and b  value is {b}")
#
#
#
#
#
# zfill method()
# str1 = "42"
#
# print(str1.zfill(5))




# practice 1
# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("Hello World"))

# practice 2
# def is_palindrome(s):
#     s = s.lower()
#     s = s[::-1]
#     return s
#
# print(is_palindrome("Madam"))  # Output: True
#



# practice 3
"aeiou"
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3






