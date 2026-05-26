#!/usr/bin/env python3

import os
import time
import random
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Clear screen safely
os.system("clear")

# Config
AUTH_KEY = "@admin/com"
SESSION_LOG = "payback_session.log"


def show_banner():
    print(f"""{Fore.RED}
██████╗  █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝
██╔══██╗██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗
██║  ██║██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Style.RESET_ALL}""")

    print(f"{Fore.CYAN}>>> Blockchain Forensic Suite v4.2 <<<{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}>>> Exclusive Payback Technology <<<{Style.RESET_ALL}\n")


def log_session(event, data=""):
    try:
        with open(SESSION_LOG, "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {event} {data}\n")
    except:
        pass


def auth():
    for attempt in range(3, 0, -1):
        try:
            key = input(
                f"{Fore.YELLOW}[?] ENTER AUTH KEY ({attempt} attempts): {Style.RESET_ALL}"
            )

            if key == AUTH_KEY:
                log_session("AUTH_SUCCESS")
                return True

            print(f"{Fore.RED}[!] INVALID KEY{Style.RESET_ALL}")
            log_session("AUTH_FAILED")

        except KeyboardInterrupt:
            print("\nAborted.")
            sys.exit(1)

    print(f"\n{Fore.RED}[!] MAXIMUM ATTEMPTS REACHED{Style.RESET_ALL}")
    time.sleep(1)
    return False


def generate_phases():
    return {
        0: "Initializing forensic engine...",
        20: "Scanning blockchain signatures...",
        40: "Analyzing transaction chain...",
        60: "Reconstructing metadata...",
        80: "Finalizing recovery sequence...",
        95: "Completing operation..."
    }


def brute_force_animation(duration=20):
    start_time = time.time()
    phases = generate_phases()

    spinner = ["|", "/", "-", "\\"]

    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        progress = min(99, int((elapsed / duration) * 100))

        current_phase = [v for k, v in phases.items() if k <= progress][-1]

        frame = spinner[int(elapsed * 10) % len(spinner)]

        print(
            f"\r{Fore.GREEN}[+] {current_phase} {frame} {progress}%",
            end="",
            flush=True
        )

        time.sleep(0.1)

    print(f"\n{Fore.GREEN}[✓] OPERATION COMPLETED{Style.RESET_ALL}")


def generate_result(wallet):
    chars = "0123456789abcdef"
    random_part = ''.join(random.choice(chars) for _ in range(24))
    return f"0x{random_part}{wallet[-6:]}"


def main():

    log_session("SESSION_STARTED")

    if not auth():
        return

    show_banner()

    try:
        wallet = input(
            f"{Fore.BLUE}[?] ENTER TARGET WALLET: {Style.RESET_ALL}"
        )

        if not wallet.startswith("0x"):
            raise ValueError("Wallet must start with 0x")

        if len(wallet) < 20:
            raise ValueError("Wallet too short")

    except Exception as e:
        print(f"{Fore.RED}[!] ERROR: {e}{Style.RESET_ALL}")
        return

    print(f"\n{Fore.YELLOW}[!] INITIATING FORENSIC RECOVERY{Style.RESET_ALL}")
    print(f"{Fore.RED}[WARNING] DO NOT INTERRUPT PROCESS{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}[i] Estimated completion: 20 seconds{Style.RESET_ALL}\n")

    brute_force_animation()

    result = generate_result(wallet)

    print(f"\n{Fore.GREEN}[✓] RECOVERY SUCCESSFUL{Style.RESET_ALL}")
    print(f"{Fore.WHITE}ACCESS KEY: {result}{Style.RESET_ALL}")

    log_session("OPERATION_COMPLETE", result)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] OPERATION ABORTED{Style.RESET_ALL}")
        sys.exit(1)
