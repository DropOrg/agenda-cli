### IMPORTS ### 
import zmq 
from pymongo import MongoClient

class AgendaSentinel(object):
	def __init__(self, in_ip, in_port, out_ip, out_port):
		self.zmq_context = zmq.Context()

		self.in_sock = context.socket(zmq.PULL)
		self.in_sock.connect("tcp://{}:{}".format(in_ip, in_port))
		self.out_sock = context.socket(zmq.PUSH)
		self.out_sock.bind("tcp://{}:{}".format(out_ip, out_port))

		self.add_cmd = 'add'
		self.rm_cmd = 'rm'
		self.upd_cmd = 'update'

		self.mongo_client = None
		self.agenda_db = None
		self.nodes = None

	def init_mongo(self, host, port):
		self.mongo_client = MongoClient(host, port)
		self.agenda_db = self.mongo_client['agenda']
		self.nodes = self.agenda_db['nodes']

	def find_availible_node(self):
		#TODO: use performance-balancer to find best node to deploy on
		return None

	def push_to_best_node(self, alias, interval):
		pass
		
	def run(self):
		while True:
			task = self.in_sock.recv_json()
			best_node_alias = self.find_availible_node()

			








		