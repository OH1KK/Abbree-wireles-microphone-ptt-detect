#!/usr/bin/env python3
import evdev
import time
import sys

# Target device name (from your evtest output)
TARGET_NAME = "KST_vHMIC010 (AVRCP)"

# Find the device automatically
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

device = None
for dev in devices:
    if TARGET_NAME in dev.name:
        device = dev
        break

if device is None:
    print(f"❌ Could not find device with name containing '{TARGET_NAME}'")
    print("Available devices:")
    for dev in devices:
        print(f"  {dev.path}: {dev.name}")
    print("\nMake sure the Abbree mic is connected and try running the script again.")
    sys.exit(1)

print(f"✅ Found and monitoring: {device.path} → {device.name}")

# Main logic
print("   Hold PTT → 'PTT pressed'")
print("   Release PTT → 'PTT released' (using KEY_REWIND value 0)\n")

ptt_active = False
last_print_time = 0
DEBOUNCE = 0.08

for event in device.read_loop():
    if event.type != evdev.ecodes.EV_KEY:
        continue

    now = time.time()

    # PTT Pressed: KEY_FASTFORWARD (value 1 or 2)
    if event.code == evdev.ecodes.KEY_FASTFORWARD:
        if event.value in (1, 2):
            if not ptt_active and (now - last_print_time > DEBOUNCE):
                print("🚀 PTT pressed (held)")
                ptt_active = True
                last_print_time = now

    # PTT Released: KEY_REWIND value 0 (as you requested)
    elif event.code == evdev.ecodes.KEY_REWIND and event.value == 0:
        if ptt_active and (now - last_print_time > DEBOUNCE):
            print("🔇 PTT released")
            ptt_active = False
            last_print_time = now

