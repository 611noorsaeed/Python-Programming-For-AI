# 1. List Comprehension
# Create a list of squares for numbers 0 to 9:

square = [x**2 for x in range(10)]
print(square)
# ====================================
# 2. Filtering Even Numbers
# Get even numbers from 0 to 19:
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
#=====================================
# 4. Dictionary Comprehension
# Create a dictionary with numbers and their squares:

dict_squares = {x: x**2 for x in range(10)}
print(dict_squares)
#===================================
# 5. Filtering with Dictionary Comprehension
# Filter a dictionary to only include items where the value is even:
dict_element = {'a':1,'b':2,'c':3,'d':4,'e':5}
even_values = {key: value for key,value in dict_element.items() if value % 2==0}
print(even_values)
#===================================
# 6. Combining Lists with Zip
# Create a list of tuples from two lists:
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
zip_lists = [(name, score) for name, score in zip(names,scores)]
print(zip_lists)
#===================================
# 7. Set Comprehension
# Create a set of unique vowels from a string:
phrase = "hellow world"
vowels = [word for word in phrase if word in "aeoui"]
print(vowels)
#===================================
# 8. Conditional Expressions
# Assign a value based on a condition:
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
#===============================
# 9 Combining Strings
# Join a list of strings with a separator:
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence)
#===============================
# 10 List of Lengths
# Get the lengths of each word in a list:
words = ['apple', 'banana', 'cherry']
lengths = [len(word) for word in words]
print(len(lengths))
#==============================
# 11 Transposing a Matrix
# Transpose a 2D list (matrix):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print('Original Matrix', matrix)
print("Transposed Matrix", transposed)