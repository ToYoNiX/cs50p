# Prompt the user for the sentence
s = input("camelCase: ")

# Remove any user error
s = s.strip()

# Create an answer variable
ans = ""

# Iterate over the string
for i in s:
    if i.isupper():
        ans += '_' + i.lower()
    else:
        ans += i

# Print the output
print(ans)
