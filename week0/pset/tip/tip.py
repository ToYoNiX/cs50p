dollars = input("How much was the meal? ")
percent = input("What percentage would you like to tip? ")

# Remove the dollar sign from the dollars input and converting it to float
dollars = float(dollars.replace('$', ''))

# Remove the percent sign from the percent input and converting it to float
percent = float(percent.replace('%', ''))

# Calculate the tip
tip = (dollars * percent) / 100

# Output the answer
print(f"Leave ${tip:.2f}")
