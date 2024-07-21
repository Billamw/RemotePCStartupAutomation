
import requests
import socket
import subprocess
import time
import sys

start_time = time.time()

punkte = 0
max_punkte = 11  # Maximale Anzahl von Punkten, bevor sie zurückgesetzt werden

try:
    while True:
        try:
            data = "test"
            print(f"\n{data}")
            # print(f"\n{data.decode()}")
            break  # Beendet die Schleife, wenn Daten empfangen wurden
        except BlockingIOError:
            punkte += 1
            if punkte <= max_punkte:
                print(".", end="", flush=True)  # Druckt einen Punkt in derselben Zeile
            if punkte == max_punkte:
                print("\r" + " " * max_punkte + "\r", end="", flush=True)  # Löscht die Punkte, indem es sie mit Leerzeichen überschreibt
                punkte = 0
            time.sleep(.75)
finally:
    
    minutes, seconds = divmod(time.time() - start_time, 60)
    print(f"took {int(minutes):02d}:{int(seconds):02d}")
    # sock.close()
    print("\nSocket closed")
    
    # time.sleep(2)
    subprocess.run('mstsc')
    sys.exit()  # Beendet das Programm
    pass