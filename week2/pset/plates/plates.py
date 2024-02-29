def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Remove any user error
    s = s.strip()

    # count the size of chars and numbers
    c = sum(1 for i in s if i.isalpha())
    n = sum(1 for i in s if i.isdigit())

    # Check for the size of the chars
    if c not in range(2, 7):
        return False

    # Check for any periods, spaces, or punctuation
    if c + n != len(s):
        return False

    # Get the first number idx
    idx = None
    for i in s:
        if i.isdigit():
            idx = i
            break

    # Check if the first number is zero
    if idx == '0':
        return False

    # Check if all numbers are in the back
    if n != 0:
        if not(s[-1].isdigit() and len(s) - n == s.find(idx)):
            return False

    return True


main()
