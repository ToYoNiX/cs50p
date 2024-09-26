# Define the main function
def main ():
    # Prompt the user for input
    s = input("Input: ")

    ans = ''
    # Iterate over each char
    for i in s:
        if i.lower() not in ['a', 'e', 'i', 'o', 'u']:
            ans += i

    # Output the answer
    print(ans)


# Call the main function
main()
