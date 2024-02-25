# Take the input string and making sure every char is lowercase
s = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Make the string usable if there is a user error
s = s.lower().strip()

# Create a boolean to store the ans
ans = False

# Check the input
if s == "42":
    ans = True
elif s == "forty-two":
    ans = True
elif s == "forty two":
    ans = True
else:
    ans = False

# Output the Ans
if ans:
    print("Yes")
else:
    print("No")
