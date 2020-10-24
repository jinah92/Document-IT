import socket

with socket.socket() as s:
    addr = ("0.0.0.0", 80)  # 전화를 받을 포트 ip/port
    s.bind(addr)
    s.listen()
    print('start server...')
    conn, addr = s.accept()  # 전화 수락
    # conn 객체: 각 클라이언트를 관리

    print(f"accept {addr[0]}:{addr[1]}")
    data = conn.recv(1024)
    conn.send('Hi this is web'.encode())
