import socket
import json
import os
import math

#10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
def floor(x):
    return math.floor(x)

# 方程式 rn = x における、r の値を計算する。
def nroot(n, x):
    return x ** (1/n)

# 文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
def reverse(s):
    return s[::-1]

#  2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
def valid_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。
def sort(strArr):
    return sorted(strArr)

def select_method_call(request):
    if request['method'] == 'floor': return floor(request['params'][0])
    if request['method'] == 'nroot': return nroot(request['params'][0], request['params'][1])
    if request['method'] == 'reverse': return reverse(request['params'][0])
    if request['method'] == 'valid_anagram': return valid_anagram(request['params'][0], request['params'][1])
    if request['method'] == 'sort': return sort(request['params'][0])
    return None

#以前の接続が残っていたらサーバーのリンクを削除する
def if_exists_remove_link(server_address):
    try:
        os.unlink(server_address)
    # サーバアドレスが存在しない場合、例外を無視します
    except FileNotFoundError:
        pass

#ソケットオブジェクトを生成する
def initial_socket(server_address):
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    return server_socket

def main():
    server_address = '/remote_procedure_server'
    if_exists_remove_link(server_address)
    server_socket = initial_socket(server_address)
    #ソケットが接続要求を待機する
    server_socket.listen(1)
    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024)
        request = json.loads(data.decode('utf-8'))

        result = select_method_call(request)

        response = json.dumps({
            "results": result,
            "result_type": type(result).__name__,
            "id": request["id"]
        })
        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()

main()