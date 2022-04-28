from config.config import Config
import requests


class BaseRequests:
    """Class for calling HTTP requests"""

    def form_url(self, url):
        """Method to concat base url and api path"""
        return Config.BASE_URL + url

    def get(self, path, *args, **kwargs):
        """Reimplementation of GET method"""
        url = self.form_url(path)
        return requests.get(url, *args, **kwargs)

    def post(self, path, params):
        """Reimplementation of POST method"""
        url = self.form_url(path)
        return requests.post(url, params)