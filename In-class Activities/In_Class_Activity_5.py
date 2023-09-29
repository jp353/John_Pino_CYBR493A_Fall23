"""
John Pino
9/29/23
In Class Activity 5

This is a program that prompts the user to choose between 2 programs.
It then runs the selected program.
"""

print("Hello, please pick an activity to run. ")
print("You can choose In-Class Acttivity 2 or In-Class Activity 3")

userChoice = input("Chosen Activity: ")

if userChoice == "2":
    import InClassActivity2
else:
    import InClassActivity3


