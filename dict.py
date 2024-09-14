# Creating a dictionary of fruits with their colors
fruit_colors = {
	"apple": "red",
	"banana": "yellow",
	"cherry": "red"
}

# Accessing the color of an apple
apple_color = fruit_colors["apple"]
print(apple_color)  # Output: red

# Changing the color of a banana
fruit_colors["banana"] = "green"
print(fruit_colors)  # Output: {'apple': 'red', 'banana': 'green', 'cherry': 'red'}

# Adding a new fruit to the dictionary
fruit_colors["date"] = "brown"
print(fruit_colors)  # Output: {'apple': 'red', 'banana': 'green', 'cherry': 'red', 'date': 'brown'}

# Removing an element from the dictionary
del fruit_colors["cherry"]
print(fruit_colors)  # Output: {'apple': 'red', 'banana': 'green', 'date': 'brown'}

# Iterating through the dictionary keys and values
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}")
# Output:
# The color of apple is red
# The color of banana is green
# The color of date is brown

# Finding the length of the dictionary
length = len(fruit_colors)
print(length)  # Output: 3

# Checking if a key exists in the dictionary
if "apple" in fruit_colors:
    print("Apple is in the dictionary")
else:
    print("Apple is not in the dictionary")
# Output: Apple is in the dictionary

# Creating a dictionary using dictionary comprehension
uppercase_fruit_colors = {fruit: color.upper() for fruit, color in fruit_colors.items()}
print(uppercase_fruit_colors)  # Output: {'apple': 'RED', 'banana': 'GREEN', 'date': 'BROWN'}