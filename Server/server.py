import socket
try:
	serv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		serv_sock.bind(('127.0.0.1', 8000))
	except OSError:
		print(f"Сервер уже запущен")

	clients = []
	print(f"Сервер запущен")

	while True:
		try:
			try:
				data, addr = serv_sock.recvfrom(1024)
				if addr not in clients:
					clients.append(addr)
				print(data.decode("utf-8"))
				for client in clients:
					serv_sock.sendto(data, client)
			except OSError:
				serv_sock.close()
				break
		except ConnectionResetError:
			print(f"{client} get out")
			msg = f"{client} get out"
			clients.remove(client)
			serv_sock.sendall(str.encode(msg))
	input("")
	serv_sock.close()
except Exception:
	print(f"{Exception} is error")
	input("")