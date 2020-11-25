from bs4 import BeautifulSoup
import sys
import socket
import optparse
import requests

class Client:

	def connect(self, host, port):
		self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect((host, port))
    
  def send_to_scrape(self, webpage):
		self.connection.send(webpage.encode())
		received_data = self.receive()
		print(received_data)

	def receive(self):
		data = ""
		while True:
			try:
				data = data + self.connection.recv(1024).decode()
				return data
			except ValueError:
				continue
	
	def send_to_scrape(self, webpage):
		self.connection.send(webpage.encode())
		received_data = self.receive()
		print(received_data)

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def receive(self):
    	data = ""
    	while True:
    		try:
    			data = data + self.connection.recv(1024).decode()
    			return data
    		except ValueError:
    			continue

    def listen(self):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.bind((self.host,self.port))
        listener.listen(0)
        print("[+] Waiting for Incoming Connection")
        self.connection,address = listener.accept()
        print("[+] Got a Connection from " + str(address))

    def send(self, data):
        self.connection.send(data.encode())

    def scrape_page(self, webpage):
    	page = requests.get(webpage)
    	soup = BeautifulSoup(page.content, 'html.parser')
    	p_elems = soup.findAll('p')
    	p_count = 0
    	for node in p_elems:
    		if not node.findChildren():
    			p_count += 1
    	image_elems = soup.findAll('image')
    	image_count = len(image_elems)
    	result = "Count of image tags: " + str(image_count) + "\nCount of leaf paragragh tags: " + str(p_count)
    	return result


    def run(self):
    	self.listen()
    	received_data = self.receive()
    	print("[+] Scraping web page...")
    	result = self.scrape_page(received_data)
    	self.send(str(result))
    	print("[+] Done!")

def main():
	parser = optparse.OptionParser()
	parser.add_option("-p", metavar="PORT", type= int, help="port on which server listens")
	if sys.argv[1] == "client":
		parser.add_option("--host", dest = "host", help="ip address of server")
		parser.add_option("--webpage", dest = "webpage", help="Webpage url to scrape")
	(options,arguments) = parser.parse_args()
	if sys.argv[1] == "client":
		client = Client()
		client.connect(options.host, options.p)
		client.send_to_scrape(options.webpage)
	else:
		server = Server(options.p)
		server.run()

if __name__=="__main__":
	main()
