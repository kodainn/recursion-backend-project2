import os
import socket

socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

#クライアント側のソケットのアドレス
address = '/local_chat_client'

#サーバー側のソケットのアドレス
server_address = '/local_chat_server'

try:
    # もし前回の実行でソケットファイルが残っていた場合、そのファイルを削除します。
    os.unlink(address)
except FileNotFoundError:
    # ファイルが存在しない場合は何もしません。
    pass

#ソケットをアドレスと関連づける
socket.bind(address)

length = input('最大何文字取得するか入力して(最大4096): ')

try:
    int(length)
except ValueError:
    print('整数で入力してください。')
    exit()

#サーバー側にデータを送信
socket.sendto(length.encode(), server_address)

#サーバー側からデータを受信
data, address = socket.recvfrom(4096)

#データがあればでコードして変数に追加
data_str = data.decode()

print(data_str, len(data_str))

#ソケットを閉じる
socket.close()