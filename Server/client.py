import socket

try:
	def new_msg(client_socket : socket.socket,Nick : None,msg : str):

		_msg = f"{Nick} : {msg}"

		_commands = ("quit","ALAH AT BAR")

		if msg not in _commands:
			client_socket.sendall(str.encode(_msg))
		else:
			_msg = f"{Nick} leave from this server"
			client_socket.sendall(str.encode(_msg))
			while True:
				input("")

		pass

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client_socket.connect(('127.0.0.1', 8000))
	Nick = input("NickName : ")
	connection_msg = f"< {Nick} logged at new Player >"

	client_socket.sendall(str.encode(connection_msg))

	while True:
		try:
			data = client_socket.recv(1024)

			print(data.decode("utf-8"))

			if not data:
				print("ERROR")


			#msg = input("")
			msg = "se"
			if msg != "":
				new_msg(client_socket,Nick,msg) 

		except ConnectionResetError:
			print(f"	Удаленный хост принудительно разорвал существующее подключение")

	client_socket.close()
except Exception:
	with open("Log.txt","w") as file:
		file.write(Exception)
	pass
