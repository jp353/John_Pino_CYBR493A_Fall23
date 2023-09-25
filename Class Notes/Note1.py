import maskpass
import builtins  # Import the builtins module to access the 'reversed' function

passwordInput = maskpass.askpass(prompt="Give me a password!", mask="*")
guess = False  # Corrected the capitalization of 'False'
while guess is False:
    passwordGuess = input("What is the reverse password?")
    if ''.join(reversed(passwordGuess)) == passwordInput:
        guess = True

print("Correct!")
