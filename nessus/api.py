import requests
import re
import json

class Api(object):
    def __init__(self, base_url="https://www.tenable.com"):
        self.base_url = base_url

    def search(self, term):
        url = self._build_url("plugins/search?q=\"{}\"&sort=&page=1".format(term))
        r = requests.get(url)

        return self._get_search_json(r.text)

    def _matches_found(self, body):
        return "__NEXT_DATA__" in body

    def _get_search_json(self, body):
        return json.loads(re.search(r"__NEXT_DATA__ = (.*)", body).group(1))

    def _build_url(self, path):
        return "{}/{}".format(self.base_url, path)
