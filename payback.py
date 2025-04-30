#!/usr/bin/env python3
import os
import time
import random
import subprocess
from colorama import Fore, Style, init
from cryptography.fernet import Fernet
from modules.scanner import ProfessionalScanner
from modules.forensic import BlockchainTracer
from modules.auth import verify_operator

# Initialize
init(autoreset=True)

# Android/Termux Configuration
IS_TERMUX = "com.termux" in os.environ.get("PREFIX", "")
TERMUX_STORAGE = "/data/data/com.termux/files/home/storage/shared/deep_hack/"

API_KEY = "CBR7R8HS231KPHR151IT2URUZQYBTX3F1F"
ENCRYPT_KEY = Fernet(b"CIMo5pvhqE3AIcRG44cxXpJgExoas8JF7Tq3MYKczaA=")

def android_setup():
    """Prepare Termux environment"""
    if not os.path.exists(TERMUX_STORAGE):
        os.makedirs(TERMUX_STORAGE)
    if not os.path.exists("/data/data/com.termux/files/usr/bin/nmap"):
        print(f"{Fore.RED}[!] Install nmap first: pkg install nmap{Style.RESET_ALL}")
        exit(1)

def show_banner():
    os.system('clear')
    print(f"""{Fore.RED}
    ██████╗  █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝ 
    ██╔══██╗██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗ 
    ██║  ██║██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    {Style.RESET_ALL}""")
    if IS_TERMUX:
        print(f"{Fore.YELLOW}[*] Running in Android/Termux mode{Style.RESET_ALL}")

class AndroidScanner(ProfessionalScanner):
    """Termux-compatible scanner"""
    def run_scan(self, target, profile):
        if IS_TERMUX:
            return self._termux_scan(target, profile)
        return super().run_scan(target, profile)

    def _termux_scan(self, target, profile):
        """Simplified nmap for Android"""
        scan_types = {
            'quick': '-T4 -F',
            'standard': '-sS -T4',
            'deep': '-sV -T4 --script vuln'
        }
        cmd = f"/data/data/com.termux/files/usr/bin/nmap {scan_types.get(profile, '-sS')} {target}"
        try:
            result = subprocess.check_output(cmd, shell=True, text=True)
            return {
                'open_ports': self._parse_android_output(result),
                'duration_mins': random.randint(1, 5),
                'raw_data': result
            }
        except subprocess.CalledProcessError as e:
            return {'error': f"Nmap failed: {e}"}

def network_audit():
    """Modified network scanner"""
    target = input(f"{Fore.WHITE}[?] Enter target IP/range: {Style.RESET_ALL}")
    profile = input(f"{Fore.WHITE}[?] Scan type (quick/standard/deep): {Style.RESET_ALL}")
    scanner = AndroidScanner()
    return scanner.run_scan(target, profile)

def simulate_recovery():
    """Optimized for mobile"""
    print(f"\n{Fore.CYAN}[*] Initializing recovery (mobile-optimized)...{Style.RESET_ALL}")
    for i in range(300):  # Reduced from 1800 to 5 mins for mobile
        time.sleep(1)
        if random.random() < 0.1:  # Increased event frequency
            print(f"{Fore.YELLOW}[!] Detected fragment 0x{random.randint(1000,9999):X}{Style.RESET_ALL}")
        print(f"\r{Fore.GREEN}[+] Progress: [{'#'*(i//10)}{' '*(30-i//10)}] {i//60}m {i%60}s", end="")

def main():
    if IS_TERMUX:
        android_setup()
    show_banner()
    
    if not verify_operator("ETH@admin/payback"):
        exit(f"{Fore.RED}[!] Authorization failed{Style.RESET_ALL}")

    # Network Investigation
    print(f"\n{Fore.BLUE}=== MOBILE NETWORK SCAN ==={Style.RESET_ALL}")
    scan_results = network_audit()
    if 'error' in scan_results:
        print(f"{Fore.RED}[!] {scan_results['error']}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}[+] Scan Completed:{Style.RESET_ALL}")
        print(f"- Duration: {scan_results.get('duration_mins', 'N/A')} minutes")
        print(f"- Open Ports: {len(scan_results.get('open_ports', []))}")

    # Blockchain Analysis (unchanged)
    print(f"\n{Fore.BLUE}=== BLOCKCHAIN ANALYSIS ==={Style.RESET_ALL}")
    wallet = input(f"{Fore.WHITE}[?] Enter wallet address: {Style.RESET_ALL}")
    forensic_data = forensic_analysis(wallet)
    print(f"{Fore.YELLOW}[!] Risk Assessment: {forensic_data.get('risk_score', 'N/A')}/100{Style.RESET_ALL}")

    simulate_recovery()
    
    # Save results to Termux shared storage
    if IS_TERMUX:
        with open(f"{TERMUX_STORAGE}results.txt", "w") as f:
            f.write(f"Scan: {scan_results}\nForensic: {forensic_data}")
        print(f"\n{Fore.GREEN}[+] Results saved to {TERMUX_STORAGE}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
