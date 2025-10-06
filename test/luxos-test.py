import socket

server_addr = "0.0.0.0"

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_addr, 4028))
    s.listen(5)
    print(f"Listening on TCP port 4028...")

    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"{data.decode()}")
        conn.close()

if __name__ == "__main__":
    main()
