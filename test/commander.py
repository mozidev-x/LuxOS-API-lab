import socket
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <hostname>")
        sys.exit(1)
    
    hostname = sys.argv[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:    
        s.connect((hostname, 4028))
        s.send(b'{"command":"autotunerget+tempctrl+atm+version+summary+pools+config+devdetails+temps","parameter":""}')
        try:
            data = s.recv(4096)
            print(f"Received data: {data.decode()}")
            s.close()
        except socket.timeout:
            print("timeout waiting for data")
            s.close()

    except Exception as e:
        print(f"Failed to connect {hostname}:4028 - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()