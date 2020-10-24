import socket

with socket.socket() as s:
    # 주소 설정
    addr = ("www.daum.net", 80)  # 443 web
    s.connect(addr)  # 통신 시작
    s.send("GET \n".encode())  # 데이터 보내기 (웹 요청)
    data = s.recv(1024)  # 1024 바이트 데이터 받기
    print(data.decode())
