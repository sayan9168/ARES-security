import platform
import socket
import os
from datetime import datetime

def get_system_info():
    info = {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return info

if __name__ == "__main__":
    data = get_system_info()
    print("=== ARES SYSTEM INFO ===")
    for k, v in data.items():
        print(f"{k}: {v}")
