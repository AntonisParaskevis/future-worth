while True:
    try:
        # Prompt the user to enter the capital in dollars
        capital = float(input("Enter the capital in dollars\n"))
        
        # If the user has entered either zero or a negative number, prompt them to enter a valid input
        if capital <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter a number greater than zero.")

# Same for the interest in %
while True:
    try:
        interest = float(input("Enter the interest in %\n"))
        
        if interest <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter a number greater than zero.")

while True:
    # Prompt the user to enter the number of years
    years = input("Enter the number of years\n")
    
    # Check whether the user's input is valid (in this case, a positive integer). If the user has entered a letter, a punctation mark, a symbol, a non-integer number, zero, or a negative number, prompt the user to enter a valid input
    if not years.isdigit() or int(years) <= 0:
        print("Invalid entry, please enter an integer greater than zero.")
        continue
    else:
        # Convert the user's input to an integer, as the input itself is a string by default
        years = int(years)
        break
        
# Caluclate the investment's future worth, using the user's input
future_worth = capital * (1 + (interest/100))**years

# Display the investment's future worth, rounded to 2 decimals
if years == 1:
	print("The investment's worth after one year will be $" + str(future_worth) + ".")
else:
	print("The investment's worth after " + str(years) + " years will be $" + str(round(future_worth, 2)) + ".")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")