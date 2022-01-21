import socket
import keyboard

def copyToClipboard():
    with open('text.txt', 'r') as f:
        lines = f.readlines()

    keyboard.wait('CapsLock')
    for line in lines:
        keyboard.write(line, delay=0.095)

    with open('text.txt', 'w') as f:
        f.truncate(0)

# create a socket object
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

serversocket.bind(("Your IPV4", 9999))
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    message = clientsocket.recv(1024)

    if message.decode('ascii') == 'quit':
        break

    if message.decode('ascii') != 'copy':
        with open('text.txt', 'a') as f:
            f.write(message.decode('ascii') + '\n')
        print(message.decode('ascii'))
    else:
        copyToClipboard()
