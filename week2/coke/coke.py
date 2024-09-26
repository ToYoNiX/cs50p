# Create a variable for the amount due
amount_due = 50

# Create a loop that stops when the amount due is zero or below
while amount_due > 0:
    # Output the required amount
    print("Amount Due:", amount_due)

    # Prompt the user to insert the coin in the machine
    inserted_coins = int(input("Insert Coin: "))

    # Reject the invalid amount
    if inserted_coins not in [50, 25, 10, 5]:
        continue

    # Calculate the new required amount
    amount_due -= inserted_coins

# Output the change
print("Change Owed:", abs(amount_due))
