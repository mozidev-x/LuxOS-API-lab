import socket
import time
import threading

# act as dummy miner
server_addr = "0.0.0.0"

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((server_addr, 4028))
    print("Listening on port 4028...")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received message: {data} from {addr}")
    

if __name__ == "__main__":
    main()