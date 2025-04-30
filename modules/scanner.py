import subprocess
import time
import random
import json
import os
from colorama import Fore, Style
from datetime import datetime

class AndroidScanner:
    def __init__(self):
        self.nmap_path = "/data/data/com.termux/files/usr/bin/nmap"
        self.log_dir = "/data/data/com.termux/files/home/storage/shared/deep_hack/scans/"
        self.scan_profiles = {
            'quick': '-T4 -F',
            'standard': '-sS -T4 -sV',
            'deep': '-sS -T4 -sV --script vuln -p1-1000'  # Limited port range for Android
        }
        os.makedirs(self.log_dir, exist_ok=True)

    def _run_command(self, command):
        """Execute commands safely on Android"""
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                shell=True,
                timeout=300  # 5 minute timeout
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            return "TIMEOUT"
        except Exception as e:
            return f"ERROR: {str(e)}"

    def _parse_nmap(self, output):
        """Lightweight Nmap output parser for mobile"""
        results = {
            'hosts': [],
            'services': [],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Simplified parsing for Android
        for line in output.split('\n'):
            if 'open' in line and 'port' not in line:
                parts = line.split()
                if len(parts) >= 4:
                    port_proto = parts[0].split('/')
                    results['services'].append({
                        'port': port_proto[0],
                        'protocol': port_proto[1],
                        'service': parts[2],
                        'version': ' '.join(parts[3:])[:50]  # Trim long versions
                    })
        return results

    def _save_results(self, target, results):
        """Save JSON results to Termux shared storage"""
        filename = f"scan_{target.replace('.', '_')}_{int(time.time())}.json"
        path = os.path.join(self.log_dir, filename)
        with open(path, 'w') as f:
            json.dump(results, f)
        return path.replace('/data/data/com.termux', '/sdcard')

    def _print_progress(self, phase, target):
        """Mobile-friendly progress animation"""
        for i in range(1, 11):
            print(f"\r{Fore.CYAN}[{phase}] Scanning {target} [{'#'*i}{' '*(10-i)}]", 
                  end="", flush=True)
            time.sleep(0.3)

    def run_scan(self, target, profile='standard'):
        """Android-optimized scanning workflow"""
        if profile not in self.scan_profiles:
            print(f"{Fore.RED}[!] Invalid profile. Use quick/standard/deep{Style.RESET_ALL}")
            return None

        print(f"\n{Fore.YELLOW}[⚡] Starting {profile.upper()} scan{Style.RESET_ALL}")
        
        # Phase 1: Host Discovery
        self._print_progress("1/2", target)
        ping_result = self._run_command(f"ping -c 1 {target}")
        if "1 received" not in ping_result:
            print(f"\n{Fore.RED}[!] Target unreachable{Style.RESET_ALL}")
            return None

        # Phase 2: Port Scanning
        self._print_progress("2/2", target)
        nmap_cmd = f"{self.nmap_path} {self.scan_profiles[profile]} {target}"
        scan_output = self._run_command(nmap_cmd)
        
        if "ERROR" in scan_output:
            print(f"\n{Fore.RED}[!] Scan failed: {scan_output}{Style.RESET_ALL}")
            return None

        results = self._parse_nmap(scan_output)
        saved_path = self._save_results(target, results)

        print(f"\n{Fore.GREEN}[✓] Scan completed{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[i] Results saved to: {saved_path}{Style.RESET_ALL}")
        
        return {
            'status': 'completed',
            'target': target,
            'open_ports': len(results['services']),
            'report_path': saved_path,
            'timestamp': results['timestamp']
        }

    def get_last_scan(self):
        """Retrieve most recent scan results"""
        try:
            scans = sorted(
                [f for f in os.listdir(self.log_dir) if f.endswith('.json')],
                reverse=True
            )
            if scans:
                with open(os.path.join(self.log_dir, scans[0])) as f:
                    return json.load(f)
        except Exception:
            return None
