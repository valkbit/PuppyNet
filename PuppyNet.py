import time

from Utility.Input import GatherInput
from Utility.Extra import ClearScreen
from Utility.ShowMenu import DisplayMainMenu

from Modules.StartApp import StartProgram

def handleInvalidInput(reason):
    print(f"\n{reason}")
    time.sleep(1)

def getModuleFromNumber(number):

    if not isinstance(number, int):
        handleInvalidInput("\nInvalid module number.")
        return None

    match number:
        case 1:
            return "Alias"
        case 2:
            return "Network"
        case _:
            #handleInvalidInput("\nInvalid module selected.")
            return None


def main() -> None:
    while True:
        
        DisplayMainMenu()

        moduleIn: int = GatherInput("Select module...\n> ")

        if moduleIn is None:
            handleInvalidInput("\nInvalid Module Provided, Resetting...")
            continue

        moduleName: str = getModuleFromNumber(moduleIn)
        if moduleName is None:
            handleInvalidInput("\nInvalid Module Name, Resetting...")
            continue

        break

    print(f"\nStarting module {moduleName}...")
    time.sleep(1)

    ClearScreen()
    
    StartProgram(moduleName)

if __name__ == "__main__":
    main()
