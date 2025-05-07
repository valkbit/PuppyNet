import os

def ClearScreen():
    # Check the operating system and use the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux/macOS)
        os.system('clear')
