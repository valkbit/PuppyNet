import time
import subprocess
import platform

from Utility.Input import GatherInput
from Utility.ShowMenu import DisplayNetworkScreen
from Utility.Extra import ClearScreen

def handleInvalidInput(r):
    print(f"\n{r}")
    time.sleep(3)

def is_alive_host(ip):
    p = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', p, '1', ip]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def getMode(i):
    match i:
        case 1:
            return "NMAP"
        case _:
            return None

def startMode(mode):
    match mode:
        case "NMAP":
            NetworkMapper()
        case _:
            pass

def NetworkMapper():

    def set_ip():
        while True:
            ip_input = input("Enter IP address: ").strip()
            if is_alive_host(ip_input):
                return ip_input
            else:
                print("Invalid or unreachable IP. Try again.")

    def set_depth():
    
        valid_depths = ["surface", "deep", "extreme"]
        while True:
            depth_input = input("Enter Depth [Surface / Deep / Extreme]: ").strip().lower()
            if depth_input in valid_depths:
                return depth_input.capitalize()
                
            print("Invalid depth. Try again.")

    while True:

        # Reset variables in-case of incorrectly entered options.
        ip = None
        depth = "Surface"  # default
    
        ClearScreen()
        print("\n[NetworkMapper] Configure Scan:\n")
        ip = set_ip()

        print("Would you like to set a depth? (Default is Surface)")
        if input("(y/n): ").strip().lower() == 'y':
            depth = set_depth()

        print(f"\nSelected Options:\n- IP: {ip}\n- Depth: {depth}")
        
        if input("Are these correct? (y/n): ").strip().lower() == 'y':
            break
        else:
            print("Restarting setup...")
            time.sleep(2)

    start_scan(ip, depth)

def start_scan(ip, depth):
    print(f"\nScanning {ip} at {depth} depth...")
    time.sleep(2)
    # Dummy logic
    print("Scan complete.\n")

# App entry point as designated in Modules/StartApp.py
def StartModule():
    while True:
        DisplayNetworkScreen()

        modeIn = GatherInput("\nEnter Mode...\n>")

        if modeIn is None:
            handleInvalidInput("Invalid Mode Selected.")
            continue
        
        mode = getMode(modeIn)

        if mode is None:
            handleInvalidInput("Invalid Mode String Recieved.") # Realistically, you won't be getting this error.
            continue

        break
        
    startMode(mode) # Add status code in function, possibly. eg return None, x = startMode(mode) if x is None: do_something()
