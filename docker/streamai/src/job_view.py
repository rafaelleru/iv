from pyramid.httpexceptions import HTTPOk
from pyramid.view import view_config, view_defaults

# from sampleproject.models import DBSession, Post, PostSchema

from job import Job

_JOBS = []

@view_defaults(renderer='json', route_name='jobs')
class JobView(object):
    def __init__(self, request):
        self.request = request
        # Only load a single blog post when we have a post id:

    @view_config(route_name='jobs_collection', request_method='GET')
    def get_jobs(self):
        return [job.to_db_object() for job in _JOBS]

    @view_config(route_name='jobs_collection', request_method='POST')
    def create_post(self):
        job = Job()
        job._id = rand_id()
        job._description = rand_str()
        _JOBS.append(job)
        return
