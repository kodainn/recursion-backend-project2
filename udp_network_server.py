import socket

#AF_INETを使用してUDPソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 9001
print('starting up on port {}'.format(server_port))

#ソケットを特殊なアドレスとポート9001に紐付ける
sock.bind((server_address, server_port))

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('reveived {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('send {} bytes back to {}'.format(sent, address))