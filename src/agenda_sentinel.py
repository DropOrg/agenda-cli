### IMPORTS ### 
import zmq 
from pymongo import MongoClient

class AgendaSentinel(object):
	def __init__(self, in_ip, in_port):
		self.zmq_context = zmq.Context()

		self.in_sock = self.zmq_context.socket(zmq.PULL)
		self.in_sock.connect("tcp://{}:{}".format(in_ip, in_port))
		self.out_sock = self.zmq_context.socket(zmq.PUSH)

		self.add_node_cmd = 'add_n'
		self.rm_node_cmd = 'rm_n'

		self.mongo_client = None
		self.agenda_db = None
		self.nodes = None

	def init_mongo(self, host, port):
		self.mongo_client = MongoClient(host, port)
		self.agenda_db = self.mongo_client['agenda']
		self.nodes = self.agenda_db['nodes']

	def add_node(self, alias, ip, port):
		pass

	def rm_node(self, alias):
		pass

	def find_availible_node(self):
		#TODO: use performance-balancer to find best node to deploy on
		return (None, None, None)
		
	def run(self):
		while True:
			task = self.in_sock.recv_json()
			cmd = task['cmd']

			if cmd == self.add_node_cmd:
				self.add_node(task['alias'], task['ip'], task['port'])
			elif cmd == self.rm_node_cmd:
				self.rm_node(task['alias'])
			else:
				alias, ip, port = self.find_availible_node()
				self.out_sock.bind("tcp://{}:{}".format(ip, port))
				self.out_sock.send_json(task)





			








		