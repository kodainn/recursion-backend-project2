const net = require('net');

// PythonのRPCサーバーのアドレス
const serverAddress = '/remote_procedure_server';

// リクエストデータ
const requestList = [
    {
        id: 1,
        method: 'floor',
        param_types: ['floor'],
        params: [3.7]
    },
    // {
    //     id: 2,
    //     method: 'nroot',
    //     param_types: ['int', 'int'],
    //     params: [5, 4]
    // },
    // {
    //     id: 3,
    //     method: 'reverse',
    //     param_types: ['string'],
    //     params: ['あいうえお']
    // },
    // {
    //     id: 4,
    //     method: 'valid_anagram',
    //     param_types: ['string', 'string'],
    //     params: ['abc', 'abc']
    // },
    // {
    //     id: 5,
    //     method: 'sort',
    //     param_types: ['list'],
    //     params: [[4, 3, 6, 2, 1, 5]]
    // },
];

// ソケット接続
const client = net.createConnection(serverAddress);

client.on('connect', () => {
    console.log('Connected to Python RPC server');
    
    // リクエスト送信
    client.write(JSON.stringify(requestList[0]));
});

client.on('data', (data) => {
    const responseData = JSON.parse(data);
    console.log('Received response from Python RPC server:', responseData);
});

client.on('end', () => {
    console.log('Disconnected from Python RPC server');
});