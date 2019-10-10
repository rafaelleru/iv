from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from pyramid.view import view_config, view_defaults

from src.job import Job

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

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('jobs_collection', '/')
        config.add_route('post_job', '/job')
        config.scan()
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 80, app)
    server.serve_forever()
