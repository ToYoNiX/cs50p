# Prompts the user for a greeting
greeting = input("Greeting: ")

# Remove any user error from the input
greeting = greeting.lower().strip()

# Create an answer variable
ans = 0

if greeting.find("hello") == 0:
    ans = 0
elif greeting[0][0] == 'h':
    ans = 20
else:
    ans = 100

# Output the answer
print(f"${ans}")
