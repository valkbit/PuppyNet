import importlib
import os
from pathlib import Path

def CheckUsername(name):
    found_accounts = []

    # Get absolute path to Checkers dir
    checkers_path = Path(__file__).resolve().parent / "Checkers"

    # Loop through all Python files in Checkers dir
    for file in os.listdir(checkers_path):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"Modules.Checkers.{file[:-3]}"  # Remove .py extension
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "Start"):
                    result = module.Start(name)
                    if result and isinstance(result, (list, tuple)) and result[1] is True:
                        found_accounts.append(result[2])  # result[2] is the account link
                        print(f"[+] {name} - {module_name}")
                    if result and isinstance(result, (list, tuple)) and result[1] is False:
                        print(f"[-] {name} - {module_name}")
            except Exception as e:
                print(f"[!] Failed to load {module_name}: {e}")

    return found_accounts
