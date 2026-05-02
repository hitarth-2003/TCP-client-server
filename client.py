import socket

if __name__=="__main__":
    ip="127.0.0.1"
    port= int(input("enter 4 digit port no you want to use:"))

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((ip,port))
    
    
    string = input("enter the data you want to send:")
    server.send(bytes(string,"utf-8"))

    buffer=server.recv(1024)
    buffer=buffer.decode("utf-8")
    print(f"SERVER:{buffer}")