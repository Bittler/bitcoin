from cachetools import cached, LRUCache
from requests import request

class Bitcoin:

    def __init__(self, url: str = "http://127.0.0.1:8332"):
        self.url = url
    
    def auth(self, username: str, password: str):
        self.username = username
        self.password = password

    def call(self, data: dict):
        return request(method="POST", url=self.url, json=data, auth=(self.username, self.password)).json().get("result")
    
    @cached(cache=LRUCache(maxsize=100))
    def validate_address(self, address: str):
        data = {"method": "validateaddress", "params": [address]}
        return self.call(data)
