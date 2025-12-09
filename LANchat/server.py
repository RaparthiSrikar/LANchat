import socket
import threading

clients = {}  # socket → username

def save_to_history(message):
    with open("chat_history.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def handle_client(conn, addr):
    username = conn.recv(1024).decode().strip()
    clients[conn] = username

    join_msg = f"- {username} joined the chat!"
    print(join_msg)
    broadcast(join_msg, conn)
    save_to_history(join_msg)

    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            formatted = f"[{username}]: {msg}"
            broadcast(formatted, conn)
            save_to_history(formatted)

        except:
            break

    # Disconnect handling
    leave_msg = f"* {username} left the chat."
    print(leave_msg)
    broadcast(leave_msg, conn)
    save_to_history(leave_msg)

    conn.close()
    del clients[conn]

def broadcast(message, sender=None):
    for client in list(clients.keys()):
        try:
            client.send(message.encode())
        except:
            client.close()
            del clients[client]

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)

    print("Server running on port 5000...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
