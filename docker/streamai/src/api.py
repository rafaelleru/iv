from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.view import view_config, view_defaults

from src.job import Job

import os

import json
import random
import string

# from job_view import JobView

_JOBS = []

@view_config(route_name='jobs_collection', request_method='GET', renderer='json')
def get_job(context, request):
    response =  Response("OK", 200)
    return response

@view_config(route_name='post_job', request_method='POST', renderer='json')
def add_job(context, request):
    job = Job()
    job._id = ''.join(random.choice(string.ascii_lowercase) for i in range(24))
    job.description = "Fake job"
    _JOBS.append(job)
    response =  Response("OK", 200)
    return response

@view_config(route_name='status', request_method='GET', renderer='json')
def status(context, request):
	response = Response(status=200, content_type='application/json')
	response.json_body = {"status": "OK"}
	return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    with Configurator() as config:
        config.add_route('jobs_collection', '/queue')
        config.add_route('post_job', '/job')
        config.add_route('status', '/status')
        config.scan()
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
