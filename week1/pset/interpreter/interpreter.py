# Prompt the user for the expression
expression = input("Expression: ")

# Getting the variables from the user
expression = expression.split()
x = int(expression[0])
y = int(expression[2])

# Calculate the ans
operator = expression[1]
if operator == '+':
    ans = x + y
elif operator == '-':
    ans = x - y
elif operator == '*':
    ans = x * y
else:
    ans = x / y

# Output the ans
print(float(ans))
