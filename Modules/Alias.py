import os
import time
from pathlib import Path
from datetime import datetime

from Utility.Input import GatherInput
from Utility.ShowMenu import DisplayAliasScreen

from Modules.Checker import CheckUsername

def handleInvalidInput(r):
    print(f"\n{r}")
    time.sleep(3)

def checkName(name):
    results = CheckUsername(name)

    log_lines = []
    for account_link in results:
        log_lines.append(account_link)

    print(f"[*] Finished scanning username {name}.")

    # Path setup
    base_dir = Path(__file__).resolve().parent.parent
    results_dir = base_dir / "results"
    results_dir.mkdir(exist_ok=True)

    # Timestamped archive
    timestamp = datetime.now().strftime("%m-%d_%H-%M")
    latest_path = results_dir / "latest.txt"
    archive_path = results_dir / f"{timestamp}.txt"

    # Save valid results
    with open(latest_path, "w") as latest, open(archive_path, "w") as archive:
        for line in log_lines:
            latest.write(line + "\n")
            archive.write(line + "\n")

    print(f"[*] Saved valid usernames to:\n- {latest_path}\n- {archive_path}")

# App entry point as designated in Modules/StartApp.py
def StartModule():
    while True:
        DisplayAliasScreen()

        modeIn = GatherInput("Enter Mode: ")
        if modeIn is None:
            handleInvalidInput("Invalid mode. Resetting...")
            return

        match modeIn:
            case 1:
                while True:
                    uname = input("Enter username: ").strip()

                    print(f"You entered '{uname}'. Is this correct?")
                    yes_no = input("(y/n): ").strip().lower()
                    if "y" not in yes_no:
                        handleInvalidInput("You selected no, returning to the start.")
                        return
                    else:
                        checkName(uname)
                        break

            case 2:
     # Phone Number. Look up specific country site, eg hitta.se for +46 and krak.dk for +45.
                pass
