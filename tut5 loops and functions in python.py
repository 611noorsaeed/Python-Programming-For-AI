# loops (for and while)
# list for loop=============
# a = [20,30,40,50]
# for i in a:
#     print(i)


# tuples for loop===========
# fruits = ('apple', 'banana', 'cherry')
# for a in fruits:
#     print(a)


# dictionary for loop===============
# fruit_prices = {'apple': 0.50,
#                 'banana': 0.30,
#                 'cherry': 0.75}
#
# # for key, value in fruit_prices.items():
# #     print(key, " ", value)
#
# for value in fruit_prices.values():
#     print(value)



# while loop=====================
# list = [10,20,30,40,50]
# index = 0
#
# while index < len(list):
#     print(list[index])
#
#     index += 1


# while with tuples================
# a = ('a','b','c')
# i = 0
#
# while i < len(a):
#     print(a[i])
#     i+=1


# while with dictionary===========================
# fruit_prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 0.75}
# items = list(fruit_prices.items())
# index = 0
#
# while index < len(items):
#    k,v =  items[index]
#    print(f"{k} and {v}")
#
#    index +=1



# ====================while loop with range
# i = 0
#
# while i < 10:
#     print(i)
#     i+=1


# functions in pyhon============================

# 1 user defined fucntions: builin
# I.D: print(), input(), sum()

# 2 user defined function:
# specific task perform

# def addition(a,b): # parameters
#     add = a + b
#     return add
#
# def substractino(a,b): # parameters
#     sub = a - b
#     return sub
# # calling function
#
# x = 10
# y = 20
# print(addition(x,y)) # argument
# print(substractino(x,y))
# abc = 20
# xyz = 30
# print(addition(abc,xyz))
# print(substractino(abc, xyz))



# default paramters

# def abc(name, age=22, gender='F'):
#     print("name :", name)
#     print("age :", age)
#     print("gender :", gender)
#
# print(abc('Noor Saeed',30, "M"))
# print(abc("Jhon"))

# # keywords arguments
# def titanic(name,age,fare, survive):
#     print(name)
#     print(age)
#     print(fare)
#     print(survive)
#
# print(titanic(name='abc',age=30,fare=3.4,survive="Yes"))
# print(titanic(name='jhon',age=30,fare=3.4,survive="No"))



# loops and if statemtns in funtions=======

def results(x):
    for i in range(x):
        print(i)

    print("===========condisiont========")

    if x > 10:
        print("wow")
    else:
        print("now")

print(results(10))








