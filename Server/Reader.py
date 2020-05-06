import socket

def new_msg(client_socket : socket.socket,Nick : None,msg : str):

	_msg = f"{Nick} : {msg}"

	client_socket.sendall(str.encode(_msg))

	pass

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('127.0.0.1', 8000))
connection_msg = f" "

client_socket.sendall(str.encode(connection_msg))

while True:
	try:
		data = client_socket.recv(1024)

		print(data.decode("utf-8"))

		if not data:
			print("ERROR")
	except ConnectionResetError:
		print(f"Удаленный хост принудительно разорвал существующее подключение")

client_socket.close()