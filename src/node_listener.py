### IMPORTS ### 
import zmq 
import subprocess 
from crontab import Crontab

class NodeListener:
	def __init__(self, in_ip, in_port, out_ip, out_port):
		self.zmq_context = zmq.Context()

		self.in_sock = context.socket(zmq.PULL)
		self.in_sock.connect("tcp://{}:{}".format(in_ip, in_port))

		self.out_sock = context.socket(zmq.PUSH)
		self.out_sock.bind("tcp://{}:{}".format(out_ip, out_port))

		self.add_cmd = 'add'
		self.rm_cmd = 'rm'
		self.upd_cmd = 'update'
		self.cron_daemon = Crontab()

	# TODO: add support for more complex jobs (e.g not just min or hour)
	def add_cron_job(self, alias, interval):
		docker_run = 'docker run {}'.format(alias)
		job = self.cron_daemon.new(command=docker_run, comment=alias)

		if interval <= 3600:
			job.minute.every((interval/60))
		elif interval <= 86400 and interval >= 3600:
			job.hour.every((interval/3600))

		self.cron_daemon.write()

	def rm_cron_job(self, alias):
		self.cron_daemon.remove_all(comment=alias)

	def update_cron_job(self, alias, interval):
		self.rm_cron_job(alias)
		self.add_cron_job(alias, interval)

	def run(self):
		while True:
			task = self.in_sock.recv_json()
			command = task['cmd']

			if command == self.add_cmd:
				self.add_cron_job(task['alias'], task['itval'])
			elif command == self.rm_cmd:
				self.rm_cron_job(task['alias'])
			elif command == self.upd_cmd:
				self.update_cron_job(task['alias'], task['itval'])




		