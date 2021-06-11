import socket
import _thread
import sys

PORT = 8080

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("\n Socket creation error \n")
    exit()

stop = 0

def client_handler():
    global sock, stop
    while(True):
        string = input()
        sock.sendall(bytes(string, "utf-8"))
        if(string == "quit"):
            print("QUIT SIIIIII\n")
            stop = 1
            break
        print("Message sent\n")


def main(addr: str):
    global sock, stop

    try:
        socket.inet_pton(socket.AF_INET, addr)
    except:
        print("\nInvalid address/ Address not supported \n")
        exit()

    try:
        sock.connect((addr, PORT))
    except:
        print("\nConnection Failed \n")
        exit()

    try:
        _thread.start_new_thread(client_handler)
    except:
        print("Create thread error!\n")

    while(True):
        buffer = str(sock.recv(1024), "utf-8")
        if(len(buffer) != 0):
            print("%s\n" % buffer)
        if(stop == 1):
            break


if __name__=="__main__":
    main(sys.argv[1])
    

