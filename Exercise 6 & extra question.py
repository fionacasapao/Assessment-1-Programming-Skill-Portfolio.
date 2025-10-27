"""
BRUTE FORCE ATTACK
with extra question
"""



CORRECT_PASSWORD = "12345" #Setting the correct password
MAX_ATTEMPTS = 5 #Setting the maximum attempts that can be done
attempts = 0

while attempts < MAX_ATTEMPTS: #user input of password
    user_input = input("Enter password: ")
    attempts += 1

    if user_input == CORRECT_PASSWORD: #user input if the password is correct
        print("Password accepted. Welcome!")
        break
    else:
        remaining = MAX_ATTEMPTS - attempts #counting or setting the remaining attempts that can be done
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.") #if the entered password reached the maximum attempts
            #authorities will be alerted

