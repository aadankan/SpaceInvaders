import socket
from _thread import *
from player import Player
from enemy import Enemy
import pickle
import random

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")


players = [Player(300, 480), Player(400, 480)]
enemies = [Enemy(random.randint(0, 736), random.randint(50, 150))]


def thread_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(thread_client, (conn, currentPlayer))
    currentPlayer += 1
