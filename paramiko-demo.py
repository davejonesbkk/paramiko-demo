from paramiko import client

class ssh:
	client = None

	def __init__(self, address, username, password):
		#let the user know we are connecting 
		print("Connecting to server")
		#create a new ssh client
		try:
			self.client = client.SSHClient()
			#needed for server not in known_hosts file
			self.client.set_missing_host_key_policy(client.AutoAddPolicy())
			self.client.connect(address, username=username, password=password, look_for_keys=False, timeout=10)
			print("Connected")
		except:
			print("Error")

	def sendCommand(self, command):
		print("Sending commands")
		#check if connection is made previously
		if(self.client):
			print()
			stdin, stdout, stderr = self.client.exec_command(command)
			alldata = stdout.channel.recv(1024)
			print(str(alldata, "utf8"))
		else:
			print("Connection not opened")

connection = ssh("192.168.1.54", "david", "password123")				
connection.sendCommand("ls /home/david")	
