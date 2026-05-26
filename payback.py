#!/usr/bin/env python3
import os
import time
import random
import sys
from colorama import Fore, Style, init

# Initialize
init(autoreset=True)
os.system('clear')

# Configuration
AUTH_KEY = "@admin/com"
SESSION_LOG = "/data/data/com.termux/files/home/storage/shared/payback_session.log"

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
    """Log all activity to external file"""
    with open(SESSION_LOG, "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {event} {data}\n")

def auth():
    """Secure authentication with lockdown"""
    for attempt in range(3, 0, -1):
        try:
            key = input(f"{Fore.YELLOW}[?] ENTER AUTH KEY ({attempt} attempts): {Style.RESET_ALL}")
            if key == AUTH_KEY:
                log_session("AUTH_SUCCESS")
                return True
            print(f"{Fore.RED}[!] INVALID KEY{Style.RESET_ALL}")
            log_session("AUTH_FAILED", f"attempt_{3-attempt}")
        except KeyboardInterrupt:
            log_session("AUTH_INTERRUPTED")
            sys.exit(1)
    
    log_session("AUTH_LOCKED")
    print(f"\n{Fore.RED}[!] MAXIMUM ATTEMPTS REACHED{Style.RESET_ALL}")
    print(f"{Fore.RED}[!] SYSTEM LOCKED{Style.RESET_ALL}")
    time.sleep(2)
    sys.exit(1)

def generate_hacking_phrases():
    """Dynamic hacking phrases with progress weighting"""
    phases = {
        0: "Initializing zero-day exploit...",
        20: "Bypassing wallet encryption...",
        40: "Cracking 2FA protection...",
        60: "Decrypting transaction history...",
        80: "Reconstructing private keys...",
        90: "Finalizing forensic evidence..."
    }
    return phases

def brute_force_animation(duration=900):
    """Realistic brute force animation"""
    start_time = time.time()
    phrases = generate_hacking_phrases()
    
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        progress = min(99, (elapsed / duration) * 100)
        
        # Select phase based on progress
        current_phase = [v for k,v in phrases.items() if k <= progress][-1]
        
        # Dynamic animation frames
        frames = ["▁▂▃▄▅▆▇█", "▏▎▍▌▋▊▉█", "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"]
        current_frame = frames[int(elapsed) % len(frames)]
        
        print(f"\r{Fore.GREEN}[+] {current_phase} {current_frame} {progress:.1f}%", end="", flush=True)
        time.sleep(0.15)
    
    print(f"\n{Fore.GREEN}[✓] OPERATION COMPLETED{Style.RESET_ALL}")

def generate_result(wallet):
    """Generate realistic forensic output"""
    chars = "0123456789abcdef"
    timestamp = hex(int(time.time()))[2:]
    wallet_snippet = wallet[-6:] if wallet else "000000"
    return f"0x{timestamp}{''.join(random.choice(chars) for _ in range(12))}{wallet_snippet}"

def main():
    # Setup environment
    os.makedirs(os.path.dirname(SESSION_LOG), exist_ok=True)
    log_session("SESSION_STARTED")
    
    # Authentication
    if not auth():
        return
    
    show_banner()
    
    # Target acquisition
    try:
        wallet = input(f"{Fore.BLUE}[?] ENTER TARGET WALLET: {Style.RESET_ALL}")
        if not wallet.startswith("0x") or len(wallet) < 20:
            raise ValueError("Invalid wallet format")
    except Exception as e:
        print(f"{Fore.RED}[!] ERROR: {e}{Style.RESET_ALL}")
        log_session("INVALID_INPUT", str(e))
        return
    
    log_session("TARGET_ACQUIRED", wallet)
    
    # Start operation
    print(f"\n{Fore.YELLOW}[!] INITIATING FORENSIC RECOVERY{Style.RESET_ALL}")
    print(f"{Fore.RED}[WARNING] DO NOT INTERRUPT THIS PROCESS{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}[i] Estimated completion: 15 minutes{Style.RESET_ALL}")
    
    brute_force_animation()
    
    # Generate results
    result = generate_result(wallet)
    print(f"\n{Fore.GREEN}[✓] RECOVERY SUCCESSFUL{Style.RESET_ALL}")
    print(f"{Fore.WHITE}ACCESS KEY: {result}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}[!] SUBMIT THIS KEY TO PAYBACK ADMINS{Style.RESET_ALL}")
    
    log_session("OPERATION_COMPLETE", result)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] OPERATION ABORTED{Style.RESET_ALL}")
        log_session("SESSION_ABORTED")
        sys.exit(1)
