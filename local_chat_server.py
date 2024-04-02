import socket
import os
from faker import Faker

#ソケット生成
socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

#サーバー側のソケットのアドレス
server_address = '/local_chat_server'

#もし前回の実行でソケットファイルに残っていたらそのファイルを削除する
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))

# ソケットにアドレスを関連づける
socket.bind(server_address)

#データの受信を待ち続ける
while True:
    #クライアント側からデータを受信
    data, address = socket.recvfrom(4096)
    fakegen = Faker('ja_JP')
    data_int = int(data.decode())
    random_text = fakegen.text(max_nb_chars=data_int)

    #クライアント側にデータを送信
    socket.sendto(random_text.encode(), address)
    