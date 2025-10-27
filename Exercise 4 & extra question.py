"""
Exercise 4
10 European Countires
With Extra Question
"""

#Capitals of European Countries
print("Welcome to the European Capitals Quiz!")
print("Type your answers — capitalization doesn’t matter.\n")
score=0

# Q1
answer = input("What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# Q2
answer = input("What is the capital of Germany? ").strip().lower()
if answer == "berlin":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Berlin.\n")

# Q3
answer = input("What is the capital of Italy? ").strip().lower()
if answer == "rome":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Rome.\n")

# Q4
answer = input("What is the capital of Spain? ").strip().lower()
if answer == "madrid":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Madrid.\n")

# Q5
answer = input("What is the capital of Portugal? ").strip().lower()
if answer == "lisbon":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Lisbon.\n")

# Q6
answer = input("What is the capital of Netherlands? ").strip().lower()
if answer == "amsterdam":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Amsterdam.\n")

# Q7
answer = input("What is the capital of Greece? ").strip().lower()
if answer == "athens":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Athens.\n")

# Q8
answer = input("What is the capital of Sweden? ").strip().lower()
if answer == "stockholm":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Stockholm.\n")

# Q9
answer = input("What is the capital of Norway? ").strip().lower()
if answer == "oslo":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Oslo.\n")

# Q10
answer = input("What is the capital of Switzerland? ").strip().lower()
if answer == "bern":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Bern.\n")

# Total Score input
if score == 10:
    print(f"Excellent! You got all {score}/10 correct!")
elif score >= 7:
    print(f"Great job! You got {score}/10 correct.")
elif score >= 4:
    print(f"Not bad! You got {score}/10 correct.")
else:
    print(f"You got {score}/10 correct. Keep practicing!")
    

    

   




