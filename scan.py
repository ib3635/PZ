import socket

host = input("Введите адрес хоста (например, 127.0.0.1): ")
ports = [80, 443, 22, 21, 8080]

for port in ports:
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        print(f"Порт {port} открыт")
    except:
        print(f"Порт {port} закрыт")
    finally:
        s.close()
