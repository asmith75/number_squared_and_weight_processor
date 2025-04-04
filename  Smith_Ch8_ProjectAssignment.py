# Q1: Squaring numbers entered by the user
numbers = []

# Ask how many numbers the user wants to enter
n = int(input("How many numbers would you like to enter to square? "))

# Loop for input and validation
for i in range(n):
    while True:
        user_input = input(f'Enter number {i+1}: ')
        if user_input.isdigit():
            number = int(user_input)
            numbers.append(number)
            break  # Exit the loop if valid input is received
        else:
            print("Invalid input. Please enter a valid number.")

# Squaring the numbers
squared_numbers = [num ** 2 for num in numbers]

# Printing the results
print("The numbers you entered are: ", numbers)
print("The squared numbers are: ", squared_numbers)


# Q2-Part1: Weights input and display
weights = []

# Collect weights from the user
for i in range(1, 5):
    weight = float(input(f"Enter weight {i}: "))
    weights.append(weight)

# Displaying weights
for i in range(1, 5):
    print(f"Weight {i} is: {weights[i-1]:.2f}")  # Corrected index reference

# Display all weights as a list
print(f"\nWeights: {weights}")


# Q2-Part2: Calculating and displaying average, max weight, and selecting a weight
average_weight = sum(weights) / len(weights)
print(f"The average weight: {average_weight:.2f}")

max_weight = max(weights)
print(f"Max weight: {max_weight:.2f}")

# Allow user to select a weight based on index input
while True:
    index_input = input("Enter a number between 1 and 4 to choose a weight: ")
    if index_input.isdigit():
        index = int(index_input)
        if 1 <= index <= 4:
            print(f"Weight at position {index} is: {weights[index-1]:.2f}")
            break  # Exit the loop after displaying the selected weight
        else:
            print("Invalid input. Please enter a valid number between 1 and 4.")
    else:
        print("Invalid input. Please enter a whole number.")

# Sorting the weights in descending order
weights.sort(reverse=True)
print(f"The weights in heaviest to lightest order: {weights}")
