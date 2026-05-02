import socket

if __name__=="__main__":
    ip="127.0.0.1"
    port= int(input("enter 4 digit port no you want to use:"))

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)

    while True:
        client,address=server.accept()
        print(f"the connection established - {address[0]}:{address[1]}")

        string=client.recv(1024)
        string=string.decode("utf-8")
        string=string.upper()

        client.send(bytes(string,"utf-8"))

        client.close()
# gvfffv
# ffffffv
sdcdvdfvvcvvcv
#  vfvffvgfgb
jgrnjgtrnjgtrjngtr