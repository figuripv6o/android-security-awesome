chmod +x termux_buzz.py
python termux_buzz.py# termux_buzz.py
import os
import time

def buzz_local():
    # Replace this with an actual Bluetooth write command via an external tool or script
    os.system("termux-vibrate -d 500")  # 0.5 second vibration as a placeholder

if __name__ == "__main__":
    try:
        while True:
            print("[BUZZ] Triggered local device buzz!")
            buzz_local()
            print("[WAIT] 20 seconds before next buzz.")
            time.sleep(20)
    except KeyboardInterrupt:
        print("Stopped BUZZ loop.")
