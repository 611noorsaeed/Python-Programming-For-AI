# 1 if-else Statement
# x = 20
# if x > 30:
#     print("X is greater")
# else:
#     print("X is not greater")
#
# x = 10
# if x > 20 and x==10:
#     print("that's good")
# if x <5 and x < 3:
#     print("also that's good")
# else:
#     print("that's not good")


# 2 nested if else statement
# x = 20
# if x > 10:
#     print("Yes its' greater than 10")
#     if x > 15:
#         print("Yes its also greater than 15")
#     else:
#         print("No its not greater than 15")
# else:
#     print("N its' not greater than 10")


# elif statement
# Simple Calculator using if-elif-else
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1,2,3,4)..."))

if choice==1:
    num1 = int(input("Enter 1st number...."))
    num2 = int(input("Enter 2nd number...."))
    print(f"Add = {num1 + num2}")
elif choice==2:
    num1 = int(input("Enter 1st number...."))
    num2 = int(input("Enter 2nd number...."))
    print(f"Sub = {num1 - num2}")

elif choice==3:
    num1 = int(input("Enter 1st number...."))
    num2 = int(input("Enter 2nd number...."))
    print(f"Mult = {num1 * num2}")
elif choice==4:
    num1 = int(input("Enter 1st number...."))
    num2 = int(input("Enter 2nd number...."))
    print(f"Div = {num1 / num2}")

else:
    print("Please select correct choice....")







