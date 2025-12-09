import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            print("Disconnected from server.")
            break

def main():
    server_ip = input("Enter Server IP: ")
    username = input("Enter your username: ").strip()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((server_ip, 5000))
        print("Connected to server!")
    except:
        print("Connection failed!")
        return

    # Send username first
    client.send(username.encode())

    # Start thread to receive messages
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # Sending loop
    while True:
        msg = input("")
        if msg.lower() == "exit":
            client.close()
            break

        client.send(msg.encode())

if __name__ == "__main__":
    main()
