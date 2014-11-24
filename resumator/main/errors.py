from . import main

class ResumeNotFound(Exception):
    status_code = 404
    detail = 'Resume Not Found!'

    def __init__(self, detail=None):
        if detail is not None:
            self.detail = detail

    def __str__(self):
        return self.detail

@main.app_errorhandler(ResumeNotFound)
def handle_missing_resume(error):
    return error.detail, error.status_code
