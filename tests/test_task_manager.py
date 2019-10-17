import pytest
from src.task_manager import TaskManager


class TestTaskManager():

	def test_add_job(self):
		tm = TaskManager()
		tm.add_job({"id": "test_id"})

		assert len(tm.task_queue.keys()) == 1
		assert len(tm.task_queue["test_id"]) == 1
		assert tm.task_queue["test_id"] == [{"id": "test_id"}]

	def test_get_jobs(self):
		tm = TaskManager()

		assert tm.get_jobs() == []


	def test_get_user_jobs(self):
		tm = TaskManager()
		tm.add_job({"id": "test_id"})

		assert tm.get_user_jobs("test_id") == [{"id": "test_id"}]
		assert tm.get_user_jobs("test_id_not_exist") == []

	def test_get_n_jobs(self):
		tm = TaskManager()
		tm.add_job({"id": "test_id"})
		tm.get_n_jobs("non_existent_id") == 0
		tm.get_n_jobs("test_id") == 1

	def test_get_queued_jobs(self):
		tm = TaskManager()

		assert tm.get_queued_jobs() == 0

		tm.add_job({"id": "test_id"})

		assert tm.get_queued_jobs() == 1
