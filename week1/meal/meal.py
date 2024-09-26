def main():
    # Prompt the user for the time
    time = input("What time is it? ")

    # Convert the time to a usable format
    time = convert(time)

    # Getting the ans
    if time >= 7 and time <= 8:
        ans = "breakfast time"
    elif time >= 12 and time <= 13:
        ans = "lunch time"
    elif time >= 18 and time <= 19:
        ans = "dinner time"
    else:
        ans = ''

    # Output the ans
    print(ans)


def convert(time):
    # Remove any user error
    time = time.strip()

    # Get the hours and minutes
    time = time.replace(':', ' ')
    time = time.split()
    hours = int(time[0])
    minutes = int(time[1])

    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
