### IMPORTS ###
import zmq

class AgendaClient:
	def __init__(self, ip, port):
		self.zmq_context = zmq.Context()
		self.out_sock = self.zmq_context.socket(zmq.PUSH)
		self.out_sock.bind("tcp://{}:{}".format(ip, port))

	# NODE OPERATION METHODS
	def add_node(self, alias, ip, port):
		job = {
		'cmd': 'add_n', 
		'alias': alias, 
		'ip': ip,
		'port': port
		}
		self.out_sock.send_json(job)

	def remove_node(self, alias):
		self.out_sock.send_json({'cmd': 'rm_n', 'alias': alias})

	# CRON JOB OPERATION METHODS
	def add_job(self, alias, interval):
		job = {
		'cmd': 'add_j', 
		'alias': alias, 
		'itval': interval
		}
		self.out_sock.send_json(job)

	def remove_job(self, alias):
		self.out_sock.send_json({'cmd': 'rm_j', 'alias': alias})

	def update_job(self, alias, interval):
		job = {
		'cmd': 'upd_j', 
		'alias': alias, 
		'itval': interval
		}
		self.out_sock.send_json(job)


		