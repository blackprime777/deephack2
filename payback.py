#!/usr/bin/env python3
import os
import time
import random
from colorama import Fore, Style, init
import base64

# Initialize
init(autoreset=True)
os.system('clear')

def show_banner():
    print(f"""{Fore.RED}
    ██████╗  █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝ 
    ██╔══██╗██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗ 
    ██║  ██║██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    {Style.RESET_ALL}""")
    print(f"{Fore.CYAN}\n    End-to-End Forensic Recovery System v3.1.4\n{Style.RESET_ALL}")

def auth():
    attempts = 0
    while attempts < 3:
        key = input(f"{Fore.YELLOW}[?] Enter Auth Key: {Style.RESET_ALL}")
        if key == "@admin/com":
            return True
        attempts += 1
        print(f"{Fore.RED}[!] Invalid Key ({attempts}/3 attempts){Style.RESET_ALL}")
    return False

def brute_force_animation(duration=900):  # 15 minutes in seconds
    phases = [
        "Bypassing Wallet Security",
        "Cracking Encryption Layers",
        "Extracting Private Keys",
        "Reconstructing Transaction History"
    ]
    
    start_time = time.time()
    while time.time() - start_time < duration:
        phase = random.choice(phases)
        percent = min(100, ((time.time() - start_time) / duration) * 100)
        
        # Dynamic loading animation
        anim = random.choice(["▓▓▓▓▓▓▓▓░░", "░░▓▓▓▓▓▓▓▓", "▓▓░░▓▓▓▓▓▓", "▓▓▓▓░░▓▓▓▓"])
        
        print(f"\r{Fore.GREEN}[+] {phase} {anim} {percent:.1f}%", end="", flush=True)
        time.sleep(0.2)
    
    print(f"\n{Fore.GREEN}[✓] Bruteforce Completed{Style.RESET_ALL}")

def generate_result():
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return "0x" + ''.join(random.choice(chars) for _ in range(20))

def main():
    if not auth():
        print(f"{Fore.RED}[!] Authentication Failed. Exiting.{Style.RESET_ALL}")
        return
    
    show_banner()
    
    wallet = input(f"{Fore.BLUE}[?] Enter Target Wallet Address: {Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}[!] Starting Forensic Recovery for {wallet}{Style.RESET_ALL}")
    print(f"{Fore.RED}[WARNING] This process will take exactly 15 minutes{Style.RESET_ALL}")
    
    brute_force_animation()
    
    result = generate_result()
    print(f"\n{Fore.GREEN}[✓] Success! Recovered Access Key:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{result}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}[!] Submit this key to Payback Admins for full access{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
