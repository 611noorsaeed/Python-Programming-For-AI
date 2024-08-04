# 1 lists and its methods

# 1.1 append method:
# fruits = ['apple','banana','cherry']
# fruits.append("orange")
# print(fruits)


# 1.2 Extend Method:
# fruits = ["apple", "banana", "cherry"]
# more_fruits = ['f1','f2']
# fruits.extend(more_fruits)
# print(fruits)


# 1.3 Insert Method
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(0, "orange")
# print(fruits)


# 1.4 Remove method
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)

# 1.5 Pop:
# fruits = ["apple", "banana", "cherry"]
# fruits.pop(1)
# print(fruits)


# 1.6 clear
# a = [1,2,3,4,5]
# print(a)
# a.clear()
# print("After clear",a)


# 1.7 index
# fruits = ["apple", "banana", "cherry"]
# index = fruits.index("banana")
# print(index)  # Output: 1


# 1.8 count
# fruits = ["apple", "banana", "cherry", "banana"]
# count = fruits.count("banana")
# print(count)  # Output: 2


# 1.9 sort and revers
# a = [1,3,2,10,8,4,6,5]
# print('Not sorted list :',a)
# a.reverse()
# print("sorted list", a)


# 10 copy
# a = [1,2,3]
# b = a.copy()
# print(a)
# print(b)

# 2 tuples and its methods
# a = (1,2,3,2,4,5)
# print(a.count(2))
# print(a.index(3))




# 3 Dictionaries and its methods

# jhon_record = {
#     "name":['abc','xyz','khan'],
#     "age":[10,22,30],
#     "score":[3.4,4.1,2.1]
# }
# print(jhon_record)



# 1 clear

capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome"}
print(capitals)
capitals.clear()
print(capitals)

# 2 copy


# 3 fromkeys
# keys = ('a', 'b', 'c')
# value = 20
# new_dict = dict.fromkeys(keys, value)
# print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


# 4 get
capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome"}
# capital = capitals.get("Germany")
# print(capital)  # Output: Berlin

# 5 item
print(capitals.items())
# 8 keys
print(capitals.keys())
# 9 values
print(capitals.values())




