import random

def generate_numbers():
    # Generate 20 random integers between 1 and 100
    numbers = [random.randint(1, 100) for i in range(20)]
    return numbers

def find_lowest(numbers):
    # Find the lowest number
    lowest = min(numbers)
    return lowest

def find_highest(numbers):
    # Find the highest number
    highest = max(numbers)
    return highest

def find_total(numbers):
    # Find the sum of the numbers
    total = sum(numbers)
    return total
  
def find_average(numbers):
  # Find the average of the numbers
    average = sum(numbers)/len(numbers)
    return average

# Call the generate_numbers function to get 20 random integers
numbers = generate_numbers()

print("Here are the Random Numbers")
print ("-" * 50)
# Print the numbers
print("Random numbers:", numbers)
print ("-" * 50)

# Call the find_lowest function to find the lowest number
lowest = find_lowest(numbers)
print("Lowest number:", lowest)

# Call the find_highest function to find the highest number
highest = find_highest(numbers)
print("Highest number:", highest)

# Call the find_total function to find the sum of the numbers
total = find_total(numbers)
print("Sum of numbers:", total)

# Call the find_average function to find the average of the numbers
average = find_average(numbers)
print("The Average The Numbers Is:", average)
