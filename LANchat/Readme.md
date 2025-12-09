## README.md (quick start)

````
# LANChat

A simple LAN chat messenger using Python sockets.

## Requirements
- Python 3.7+

## How to run
1. On one machine (server) in the same LAN run:
   ```bash
   python server.py
````

2. On each client machine (same LAN) run:

   ```bash
   python client.py
   ```

   Enter the server IP when prompted (example: 192.168.29.172) and your nickname.

3. Start chatting! Type `/quit` to leave.

## Notes

* Use your machine's local IP for other clients to connect (use `ipconfig` on Windows or `ip addr` on Linux).
* The project is console-based for simplicity. You can extend it with GUI (Tkinter/PyQt), encryption, persistence, or rooms.

## Enhancements you can add

* Message history saved to SQLite
* Private messaging commands (e.g. `/pm nick message`)
* Chat rooms / channels
* TLS encryption using `ssl` module
* Web UI using WebSockets (FastAPI + JS)

```

---

## Want me to generate one of these enhancements now?
I can implement any of the following next (pick one):

1. GUI (Tkinter) client
2. Private messaging (`/pm`) feature on server & client
3. Persist chat history to SQLite and show last N messages on connect
4. TLS-encrypted server + client using `ssl` wrapping
5. WebSocket version (FastAPI server + simple HTML/JS client)

Reply with the number and I'll add it to the project.

```
