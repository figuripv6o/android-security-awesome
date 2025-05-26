#!/data/data/com.termux/files/usr/bin/bash
echo "[SECURITY AWESOME] Scan started..." | tee logs/scan_$(date +%Y%m%d_%H%M%S).log
find . -type f -name "*.py" -exec grep -iE "access|token|imei|mac|location|login|ble|camera|audio" {} \; >> logs/scan_$(date +%Y%m%d_%H%M%S).log
echo "[SECURITY AWESOME] Scan complete."
