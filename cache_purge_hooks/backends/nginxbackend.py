import requests
from django.conf import settings

def _build_url(path):    
    return path

class NginxManager(object):
    def purge(self, path):
        host_header = getattr(settings, 'NGX_CACHE_PURGE_HOST_HEADER', None)
        if host_header:
            response = requests.request("PURGE", _build_url(path), headers={'Host':host_header})
        else:
            response = requests.request("PURGE", _build_url(path))
        return response.status_code == 200
