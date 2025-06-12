#送信元のIPとポートを返すだけのシンプルなUDPサーバ

import socket

#IPアドレスとポート番号の設定
UDP_IP = "0.0.0.0"
UDP_PORT = 25566

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print(f"UDPサーバが起動しました {UDP_IP}:{UDP_PORT}")

    while True:
        #データを受信
        data, addr = sock.recvfrom(1024)
        print(f"受信データ: {data.decode()} from {addr}")
    
        #応答を作成
        response = f"{addr[0]},{addr[1]}"
        sock.sendto(response.encode(), addr)

if __name__ == "__main__":
    main()