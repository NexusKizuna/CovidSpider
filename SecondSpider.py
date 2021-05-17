import requests as rq
import json
from Pool.IpPool import IpPool
from Pool.UserAgentPool import UserAgentPool
from time import sleep

class SecondSpider:
    def __init__(self):
        self.url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province='
        self.lis = []
        self.provinceName = []

    def start(self):
        pass
