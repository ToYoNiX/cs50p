# Prompt the user for the file name
name = input("File name: ")

# Remove any user error
name = name.lower().strip()

# Ans variable
ans = ""

# Check for file format
if name.find(".gif") != -1:
    ans = "image/gif"
elif name.find(".jpg") != -1 or name.find(".jpeg") != -1:
    ans = "image/jpeg"
elif name.find(".png") != -1:
    ans = "image/png"
elif name.find(".pdf") != -1:
    ans = "application/pdf"
elif name.find(".txt") != -1:
    ans = "text/plain"
elif name.find(".zip") != -1:
    ans = "application/zip"
else:
    ans = "application/octet-stream"

# Output the answer
print(ans)
