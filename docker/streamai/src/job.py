class Job(object):
	def __init__(self):
		self._id = 0
		pass

	def from_db(self, document):
		self._id = document.get('id', None)
		self.description = document.get('description', None)

	def to_db_object(self):
		return {
			'_id': self._id,
			'description': self.description
		}
