from testing.quoted_parrot_fix import frames
import os
import sys
import time

def print_frame(frame):
    # Konsole bereinigen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Jede Zeile der aktuellen Frame ausgeben
    for line in frame:
        print(line)
    time.sleep(0.5)  # Wartezeit zwischen den Frames

def animate(frames):
    try:
        while True:
            for frame in frames:
                print_frame(frame)
    except KeyboardInterrupt:
        # Beendet die Animation, wenn Ctrl+C gedrückt wird
        print("Animation beendet.")
        sys.exit()

animate(frames)