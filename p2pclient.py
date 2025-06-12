import socket
import threading

SERVER_IP = "192.0.2.0"
SERVER_PORT = 25566

def receive_data(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"受信メッセージ: {data.decode()} from {addr}")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b"hello", (SERVER_IP, SERVER_PORT))
    data, addr = sock.recvfrom(1024)
    print(f"サーバからの応答: {data.decode()}")

    print("もう一つのクライアントに貼り付ける>>>")
    print(data.decode().split(',')[0])
    print(data.decode().split(',')[1])

    p2p_ip = input("もう一つのクライアントのIPアドレスを入力してください: ")
    p2p_port = int(input("もう一つのクライアントのポート番号を入力してください: "))
    print(f"接続先: {p2p_ip}:{p2p_port}")
    
    #相手のクライアントに送信して、NATに覚えさせる
    sock.sendto(b"hello", (p2p_ip, p2p_port))

    #別スレッドでデータを受信
    receive_thread = threading.Thread(target=receive_data, args=(sock,))
    #メインスレッド終了時に自動で終了
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        message = input("送信メッセージするメッセージを入力してください: ")
        sock.sendto(message.encode(), (p2p_ip, p2p_port))
        print(f"送信メッセージ: {message} to {p2p_ip}:{p2p_port}")



if __name__ == "__main__":
    main()