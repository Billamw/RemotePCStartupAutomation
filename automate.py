import os
import sys
import time
import socket
import argparse
import requests
import subprocess


from parrot      import parrot_frames
from animations  import loading_bar
from secrect_key import secret_key

# # ArgumentParser-Objekt erstellen
# parser = argparse.ArgumentParser(description="Automate Script")
# # Argument definieren
# parser.add_argument("-p", "--parrot", action="store_true", help="Use parrot animation")

# # Argumente parsen
# args = parser.parse_args()

# # Entscheiden, welche Animation basierend auf dem Argument verwendet werden soll
# ANIMATION = parrot_frames if args.parrot else loading_bar
ANIMATION = parrot_frames if "-p" in sys.argv else loading_bar
start_time = time.time()
url = "https://llamalab.com/automate/cloud/message"
headers = {"Content-Type": "application/json"}
data = {
    "secret": secret_key,
    "to": "johan.dasbach.jd@gmail.com",
    "device": None,
    "priority": "high",
    "payload": None
}

response = requests.post(url, headers=headers, json=data)

# print(f"Status Code: {response.status_code}")
# print('Waiting for Pc to turn on...')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5005))
sock.setblocking(0)  # Setzt den Socket in den Non-Blocking-Modus

animationIndex = 0

def clear_screen():
    """Löscht den Konsolenbildschirm."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_animation_line(animation, index):
    """Druckt eine Zeile der Animation und überschreibt die vorherige."""
    print(f"\r{animation[index % len(animation)]}", end="", flush=True)
    # Beachten Sie die zusätzlichen Leerzeichen nach der Animation, um sicherzustellen,
    # dass vorherige längere Zeilen vollständig überschrieben werden.

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"\n{data.decode()}")
            break  # Beendet die Schleife, wenn Daten empfangen wurden
        except BlockingIOError:
            # print(ANIMATION[animationIndex % len(ANIMATION)], end="", flush=True)
            print_animation_line(ANIMATION, animationIndex)
            animationIndex += 1
            if animationIndex == len(ANIMATION):
                animationIndex = 0
            time.sleep(.1)
finally:
    minutes, seconds = divmod(time.time() - start_time, 60)
    print(f"took {int(minutes):02d}:{int(seconds):02d}")
    sock.close()
    print("\nSocket closed")
    subprocess.run('mstsc')
    sys.exit()  # Beendet das Programm

