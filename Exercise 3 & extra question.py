"""
Biography
with extra question
"""

# Dictionary to create the user information
user_info = {'name': 'Fiona Casapao', 'hometown': 'Dubai', 'age': 18}

# User input
user_info["name"] = input("Enter your full name: ")
user_info["hometown"] = input("Enter your hometown: ")

# Ensuring that the user enter a number for age
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():  # Check if input contains only digits
        user_info["age"] = int(age_input)  # Convert to integer
        break
    else:
        print("Please enter a valid number for age.")

# Print the information on separate lines using one print() statement
print(f"\nName: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")

