num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result = num1 + num2
print(f"The sum of, {num1} and  {num2} is: {sum_result}")

diff_result = num1 - num2
print(f"The difference of, {num1} and  {num2} is: {diff_result}")

prod_result = num1 * num2
print(f"The product of, {num1} and  {num2} is: {prod_result}")

if num2 != 0:
    quot_result = num1 / num2
    print(f"The quotient of, {num1} and  {num2} is: {quot_result}")
else:
    print("Division by zero is not allowed.")