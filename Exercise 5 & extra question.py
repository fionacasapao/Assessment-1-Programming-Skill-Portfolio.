"""
Days of the month
with extra question
"""

# Step 1: Create a dictionary that tells about the month numbers to number of days
days_in_month = {
    1: 31,  #January
    2: 28,  # February (adjusted later if leap year)
    3: 31,  #March
    4: 30,  #April
    5: 31,  #May
    6: 30,  #June
    7: 31,  #July
    8: 31,  #August
    9: 30,  #September
    10: 31, #October
    11: 30, #November
    12: 31  #December
}

# Step 2: User input for the month number
month = int(input("Enter month number (1-12): "))

# Step 3: Check if the month is valid
if 1 <= month <= 12:
    # Step 4: Check for February and leap year adjustment
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        # Step 5: Print number of days
        print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
    