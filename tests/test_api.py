import json
import requests

from src.api import *
from src.api import _JOBS

def test_add_job_POST():
	response = requests.request(url="http://localhost:8000/job", method="POST")
	assert response.status_code == 200
	assert response.text == "OK"

def test_add_job_GET():
	response = requests.request(url="http://localhost:8000/job", method="GET")
	assert response.status_code == 404

def test_add_job_PUT():
	response = requests.request(url="http://localhost:8000/job", method="PUT")
	assert response.status_code == 404

def test_get_job_GET():
	response = requests.request(url="http://localhost:8000/queue", method="GET")
	assert response.status_code == 200
	assert response.text == "OK"

def test_get_job_PUT():
	response = requests.request(url="http://localhost:8000/queue", method="PUT")
	assert response.status_code == 404

def test_get_job_POST():
	response = requests.request(url="http://localhost:8000/queue", method="POST")
	assert response.status_code == 404
	pass

def test_status_GET():
	response = requests.request(url="http://localhost:8000/status", method="GET")
	assert response.status_code == 200
	assert response.json() == {"status": "OK"}

def test_get_job():
	response = get_job(None, None)
	assert response._status == "200 OK"

def test_add_job():
	original_jobs = len(_JOBS)
	response = add_job(None, None)
	assert response._status == "200 OK"
	assert len(_JOBS) == original_jobs+1

def test_get_job():
	response = get_job(None, None)
	assert response._status == "200 OK"
