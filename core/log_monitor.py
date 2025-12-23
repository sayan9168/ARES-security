import os
from datetime import datetime

LOG_PATHS = [
    "/var/log/auth.log",
    "/var/log/secure"
]

def read_logs():
    logs_found = False
    for path in LOG_PATHS:
        if os.path.exists(path):
            logs_found = True
            with open(path, "r", errors="ignore") as f:
                lines = f.readlines()[-50:]
                analyze_logs(lines, path)
    if not logs_found:
        print("[!] No auth logs found (Termux environment)")

def analyze_logs(lines, source):
    failed = 0
    for line in lines:
        if "Failed password" in line or "authentication failure" in line:
            failed += 1

    print(f"\n=== Log Source: {source} ===")
    print(f"Failed login attempts (last 50 lines): {failed}")

    if failed >= 5:
        alert(f"Suspicious activity detected: {failed} failed logins")

from core.alert_engine import send_alert

def alert(message):
    send_alert(
        level="HIGH",
        message=message,
        source="AUTH_LOG"
    )

if __name__ == "__main__":
    read_logs()
