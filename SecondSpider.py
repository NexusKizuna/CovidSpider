import requests as rq
import json
from Pool.IpPool import IpPool
from Pool.UserAgentPool import UserAgentPool
from time import sleep

class SecondSpider:
    def __init__(self):
        self.url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province='
        self.lis = []
        self.province = ['新疆', '黑龙江', '吉林', '辽宁', '河北', '天津', '内蒙古', '北京',
                         '山东', '山西', '陕西', '宁夏', '甘肃', '青海', '西藏', '江苏', '河南',
                         '浙江', '上海', '安徽', '湖北', '重庆', '四川', '贵州', '湖南', '江西',
                         '福建', '广东', '广西', '云南', '台湾', '海南', '澳门', '香港']

    def start(self):
        pass
