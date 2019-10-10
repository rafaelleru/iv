from src.api import *
from src.api import _JOBS

def test_add_job():
	original_jobs = len(_JOBS)
	response = add_job(None, None)
	assert response._status == "200 OK"
	assert len(_JOBS) == original_jobs+1

def test_get_job():
	response = get_job(None, None)
	assert response._status == "200 OK"
