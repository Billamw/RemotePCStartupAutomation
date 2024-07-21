import socket

# Erstellen eines UDP-Sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binden des Sockets an eine Adresse und Port
sock.bind(('', 5005))

while True:
    # Warten auf eine Nachricht
    data, addr = sock.recvfrom(1024)  # Puffergröße ist 1024 Bytes
    print(f"Empfangene Nachricht: {data.decode()} von {addr}")