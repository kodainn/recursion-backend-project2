# Recursion バックエンドプロジェクト 2

- このコースでは、コンピュータネットワークの世界に飛び込みながら、クライアントサーバ分散型アプリケーションを作成します。
- パイプやソケットのプロセス間通信プログラムの作成
- プロセス
- オペレーションシステムの基礎知識(カーネル、システムコール、シェル、インターフェース、環境構築)
- データストリーム(パイプ、ソケット)

# localChatMessenger(UDP通信でのクライアントとサーバー間通信)
UDPのプロセス間通信を用いてクライアントサーバー通信するプログラム。<br>
具体的にはクライアント側は取得する最大文字数を入力しそれをサーバー側へUDP通信で送信する。サーバー側はそれを受け取りFaker<br>
で生成されたランダム文字列を応答としてクライアントに返すプログラム。

- local_chat_client.py, local_chat_server.py ファイル参照

# remoteProcedure(TCPのプロセス間通信でのRPC)
異なるプログラミング言語で書かれたクライアント(Javascript)とサーバー(Python)でのTCPを用いたプロセス間通信でのRPCプログラム。<br>
具体的にはJavascriptでリクエストデータをJSONで記述しそれをPythonでそれを受け取りリクエストデータのmethodに該当するpythonの<br>
関数を呼び出す。

# プログラムの実行方法
- cd プロジェクトディレクトリ直下
- イメージの作成 docker image build --tag ubuntu-my-custom .
- コンテナの立ち上げ docker container run --rm -it --mount type=bind,source="$(pwd)",target=/python_practice ubuntu-my-custom bash