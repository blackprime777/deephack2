# modules/auth.py
import os
from getpass import getpass
from colorama import Fore, Style

def verify_operator(auth_key):
    """Secure authentication with Android/Termux compatibility"""
    max_attempts = 3
    log_file = "/data/data/com.termux/files/home/storage/shared/deep_hack/auth_log.txt"
    
    # Create log directory if needed (Termux)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    for attempt in range(1, max_attempts + 1):
        try:
            user_input = getpass(f"{Fore.YELLOW}[?] Enter Auth Key: {Style.RESET_ALL}")
            if user_input == auth_key:
                with open(log_file, "a") as f:
                    f.write(f"Successful auth at {time.ctime()}\n")
                return True
            
            print(f"{Fore.RED}[!] {attempt}/{max_attempts} authentication failed{Style.RESET_ALL}")
            with open(log_file, "a") as f:
                f.write(f"Failed attempt {attempt} at {time.ctime()}\n")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Auth error: {e}{Style.RESET_ALL}")
            return False

    # Self-destruct after max attempts (Android security measure)
    if os.path.exists(log_file):
        os.remove(log_file)
    return False
