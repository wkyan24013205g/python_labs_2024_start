# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

# Accessing the first element
first_fruit = fruits[0]
print(first_fruit)  # Output: apple

# Changing the second element
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding a new element to the list
fruits.append("date")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing an element from the list
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'cherry', 'date']

# Iterating through the list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# cherry
# date

# Finding the length of the list
length = len(fruits)
print(length)  # Output: 3

# Slicing the list
subset = fruits[1:3]
print(subset)  # Output: ['cherry', 'date']

# Creating a list using list comprehension
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)  # Output: ['APPLE', 'CHERRY', 'DATE']