# buzz_em_all.py
import asyncio
from bleak import BleakClient, BleakScanner
import time

# Lil Baby special sauce UUID — update this if your device uses a different one
BUZZ_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
BUZZ_COMMAND = b"buzzzzzzz"  # This is the trigger command

async def buzz_device(device):
    try:
        async with BleakClient(device.address) as client:
            if await client.is_connected():
                print(f"[BUZZING] {device.name} ({device.address}) for Lil Baby!")
                await client.write_gatt_char(BUZZ_UUID, BUZZ_COMMAND)
    except Exception as e:
        print(f"[ERROR] {device.name or device.address}: {e}")

async def main():
    print("[SCAN] Searching BLE field for buzzers...")
    devices = await BleakScanner.discover()
    tasks = [buzz_device(d) for d in devices if d.name]
    await asyncio.gather(*tasks)
    print("[CYCLE DONE] Buzz storm complete for this round.")

if __name__ == "__main__":
    try:
        while True:
            asyncio.run(main())
            print("[PAUSE] Waiting 20 seconds before next round...")
            time.sleep(20)
    except KeyboardInterrupt:
        print("BUZZ EM ALL terminated. BLE quiet for now.")
