import socket

addr = ('0.0.0.0', 4444)

with socket.socket() as s:
    s.bind(addr)
    s.listen()
    print('Server is started ...')
    conn, addr = s.accept()
    print(f"client = {addr[0]}:{addr[1]}")

    while(1):
        data = conn.recv(1024)
        if data.decode() == 'q':
            print('quit connection')
            exit()  # 프로그램 종료
            
        conn.send(data)
        print(data.decode())
