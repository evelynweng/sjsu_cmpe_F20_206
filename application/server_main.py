from network.network import Network
from link.link import Link
from physical.tcp_client import Tcp_client
from physical.tcp_server import Tcp_server
from application import client_main 
#import mainCMPE206

def service(mylabel):
	#physical layer
	tcp_server = Tcp_server()
	receive_message = tcp_server.start_server()

	#while 1:
		print("server running0")
		#tcp_server = Tcp_server()
		#receive_message = tcp_server.start_server()
		print("server running1")
		# to_mac,to_label,str(mylabel),to_message
		# server coonection will close after revceving message
		# will start again when all the process below is done
		
		# link layer
		# take off to_mac
		link = Link()
		to_network_layer = link.de_header_receive_message(receive_message)
		print("server running2")
		
		# network layer
		# match to_label
		network = Network()
		to_link_layer = network.forward_message(mylabel, to_network_layer)
		print("server running3")
		print("tolinklayer:"+to_link_layer+"----")
		if to_link_layer == None:
			print("server running end")
			continue
			# got an "ACK" go back to the server_service loop
			# reopen server
		else:
			# __init client service to forward or sent message
			client_main.system_forward_message(mylabel, to_link_layer)
	

		
		






	
if __name__ == "__main__":
	service(123)