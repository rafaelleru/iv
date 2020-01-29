from collections import defaultdict

class TaskManager(object):
	def __init__(self):
		self.task_queue = defaultdict(list)

	def add_job(self, job):
		self.task_queue[job["id"]] += [job]

	def get_jobs(self):
		jobs = []
		for k, v in self.task_queue.items():
			jobs += v
		return jobs

	def get_user_jobs(self, id):
		return self.task_queue[id]

	def get_n_jobs(self, id):
		return len(self.task_queue[id])

	def get_queued_jobs(self):
		return sum(len(self.task_queue[k]) for k in self.task_queue)
