#!/usr/bin/env python3

import os
import time
import random
import sys
from colorama import Fore, Style, init

# Initialize
init(autoreset=True)
os.system("clear")

# CONFIG
AUTH_KEY = "@admin/com"
MEMBER_CODE = "we are anonymous"
SESSION_LOG = "payback_session.log"

# Fake private key (demo)
PRIVATE_KEY = "0x8f2a7e91c4d6f1b7aa20de77bb14c93f"

# =========================
# LOGGING
# =========================

def log_session(event, data=""):
    try:
        with open(SESSION_LOG, "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {event} {data}\n")
    except:
        pass


# =========================
# BANNER
# =========================

def show_banner():
    print(f"""{Fore.RED}

██████╗  █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝
██╔══██╗██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗
██║  ██║██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

{Style.RESET_ALL}""")

    print(f"{Fore.CYAN}>>> Tactical Recovery Framework v6.4 <<<")
    print(f"{Fore.YELLOW}>>> Anonymous Tactical Division <<<\n")


# =========================
# AUTH
# =========================

def auth():
    for attempt in range(3, 0, -1):

        key = input(
            f"{Fore.YELLOW}[?] ENTER AUTH KEY ({attempt} attempts): {Style.RESET_ALL}"
        )

        if key == AUTH_KEY:
            print(f"{Fore.GREEN}[✓] ACCESS GRANTED\n")
            log_session("AUTH_SUCCESS")
            return True

        print(f"{Fore.RED}[!] INVALID KEY\n")
        log_session("AUTH_FAILED")

    return False


# =========================
# ASCII HOODIE
# =========================

def hoodie_face():

    print(f"""{Fore.GREEN}

            .----.
         _.'__    `.
     .--(#)(##)---/#\\
   .' @          /###\\
   :         ,   ##### 
    `-..__.-' _.-\\###/
          `;_:    `"'
        .'"""""`.
       /,  PAYBACK ,\\
      // Tactical \\\\
      `-._______.-'

{Style.RESET_ALL}""")


# =========================
# ANIMATION
# =========================

def fake_hack(duration, phases):

    spinner = ["|", "/", "-", "\\"]

    start = time.time()

    while time.time() - start < duration:

        elapsed = time.time() - start
        progress = int((elapsed / duration) * 100)

        phase = [v for k, v in phases.items() if k <= progress][-1]

        frame = spinner[int(elapsed * 10) % len(spinner)]

        print(
            f"\r{Fore.GREEN}[+] {phase} {frame} {progress}%",
            end="",
            flush=True
        )

        time.sleep(0.1)

    print(f"\n{Fore.GREEN}[✓] PROCESS COMPLETE\n")


# =========================
# KILL ORDER
# =========================

def kill_order():

    print(f"{Fore.RED}[!] DEPLOYING KILL ORDER...\n")

    phases = {
        0: "Routing through dark relay nodes...",
        20: "Injecting NSA bypass payload...",
        40: "Overriding satellite firewall...",
        60: "Deploying anonymous execution chain...",
        80: "Finalizing tactical strike..."
    }

    fake_hack(20, phases)

    print(f"{Fore.RED}[✓] KILL ORDER DEPLOYED SUCCESSFULLY")
    print(f"{Fore.YELLOW}[i] TARGET SYSTEM NEUTRALIZED\n")


# =========================
# EXPLOIT
# =========================

def exploit_sequence():

    print(f"{Fore.CYAN}[!] INITIATING EXPLOIT RECOVERY...\n")

    phases = {
        0: "Scanning blockchain footprint...",
        20: "Decrypting shadow ledger...",
        40: "Extracting exploit channels...",
        60: "Recovering target metadata...",
        80: "Generating recovery output..."
    }

    fake_hack(20, phases)

    print(f"{Fore.GREEN}[✓] PRIVATE KEY RECOVERED\n")

    print(f"{Fore.WHITE}PRIVATE KEY:")
    print(f"{Fore.YELLOW}{PRIVATE_KEY}\n")


# =========================
# MAIN
# =========================

def main():

    show_banner()

    if not auth():
        print(f"{Fore.RED}[!] ACCESS DENIED")
        return

    wallet = input(
        f"{Fore.BLUE}[?] ENTER TARGET WALLET: {Style.RESET_ALL}"
    )

    print(f"\n{Fore.RED}[!] ADDRESS PROFILING ERROR x5")
    time.sleep(1)

    hoodie_face()

    code = input(
        f"{Fore.YELLOW}[?] ENTER MEMBER CODE: {Style.RESET_ALL}"
    )

    if code.lower() != MEMBER_CODE:
        print(f"{Fore.RED}[!] INVALID MEMBER CODE")
        return

    print(f"\n{Fore.GREEN}[✓] INFILTRATION SYSTEM DEPLOYED\n")

    phases = {
        0: "Connecting to anonymous relay...",
        20: "Establishing encrypted tunnel...",
        40: "Scanning blockchain activity...",
        60: "Deploying exploit framework...",
        80: "Analyzing target signature..."
    }

    fake_hack(15, phases)

    print(f"{Fore.GREEN}[✓] TARGET FOUND\n")

    print(f"{Fore.CYAN}[1] INITIATE KILL ORDER")
    print(f"{Fore.CYAN}[2] INITIATE EXPLOIT\n")

    choice = input(f"{Fore.YELLOW}[?] SELECT OPTION: {Style.RESET_ALL}")

    if choice == "1":
        kill_order()

    elif choice == "2":
        exploit_sequence()

    else:
        print(f"{Fore.RED}[!] INVALID OPTION")


# =========================
# START
# =========================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] OPERATION ABORTED")
        sys.exit(1)
