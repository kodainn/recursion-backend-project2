# Recursion バックエンドプロジェクト 2

- このコースでは、コンピュータネットワークの世界に飛び込みながら、クライアントサーバ分散型アプリケーションを作成します。
- パイプやソケットのプロセス間通信プログラムの作成
- プロセス
- オペレーションシステムの基礎知識(カーネル、システムコール、シェル、インターフェース、環境構築)
- データストリーム(パイプ、ソケット)

# localChatMessenger(UDP通信でのクライアントとサーバー間通信)

- local_chat_client.py, local_chat_server.py ファイル参照

# プログラムの実行方法
- cd プロジェクトディレクトリ直下
- イメージの作成 docker image build --tag ubuntu-my-custom .
- コンテナの立ち上げ docker container run --rm -it --mount type=bind,source="$(pwd)",target=/python_practice ubuntu-my-custom bash