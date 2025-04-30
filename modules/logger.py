import os
import time
from cryptography.fernet import Fernet
from colorama import Fore, Style

# Android/Termux configuration
LOG_DIR = "/data/data/com.termux/files/home/storage/shared/deep_hack/logs/"
KEY = b"CIMo5pvhqE3AIcRG44cxXpJgExoas8JF7Tq3MYKczaA="  # Same key as original

class SecureLogger:
    def __init__(self):
        """Initialize logger with Termux-compatible paths"""
        os.makedirs(LOG_DIR, exist_ok=True)
        self.cipher = Fernet(KEY)
        self.log_file = os.path.join(LOG_DIR, f"payback_{int(time.time())}.enc")

    def encrypt(self, data):
        """Mobile-optimized encryption with error handling"""
        try:
            return self.cipher.encrypt(data.encode())
        except Exception as e:
            print(f"{Fore.RED}[LOGGER] Encryption failed: {e}{Style.RESET_ALL}")
            return b""

    def write(self, *args):
        """Atomic write operation with rotation"""
        try:
            log_entry = f"{time.ctime()} | {' '.join(str(arg) for arg in args)}"
            encrypted = self.encrypt(log_entry)
            
            with open(self.log_file, "ab") as f:
                f.write(encrypted + b"\n")
                
            # Rotate logs if >5MB (Android storage optimization)
            if os.path.getsize(self.log_file) > 5_242_880:  # 5MB
                self.log_file = os.path.join(LOG_DIR, f"payback_{int(time.time())}.enc")
                
        except Exception as e:
            print(f"{Fore.RED}[LOGGER] Write failed: {e}{Style.RESET_ALL}")

    def export_logs(self):
        """Get path to latest log file (for sharing)"""
        return self.log_file.replace("/data/data/com.termux", "/sdcard")
