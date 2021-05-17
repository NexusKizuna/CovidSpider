# !D:\Python37\python.exe
# _*_ coding:utf-8 _*_

import requests as rq
from time import sleep
from random import randint, random
from Pool.UserAgentPool import UserAgentPool
from Pool.IpPool import IpPool
import re
from pandas import DataFrame
from os import mkdir
from os.path import exists
from SpiderClass import Spider


class DataSpider(Spider):
    def __init__(self):
        self.url = 'http://www.sy72.com/covid/list.asp?id='
        self.lis = []

    def start(self, n):
        header = UserAgentPool()
        proxy = IpPool()
        for i in range(n):
            ip = ''
            try:
                ip = proxy.getIp()
                r = rq.get(self.url + str(i + 1) + '&s1=0&s2=0',
                           headers=header.getUserAgent(), proxies=ip)
                r.encoding = 'utf-8'
                self.lis.append(r.text)
                sleep(randint(2, 5) + random())
            except:
                proxy.removeIp(ip)
                sleep(randint(3, 10))
                i = i-1
        return self.getData()

    def getData(self):
        data = {}
        for ii in range(len(self.lis)):
            name = re.findall(r"最新 (.*?) 疫情", self.lis[ii])[0]
            diagnosis = re.findall("<span class=\"c1\">(.*?)</span>", self.lis[ii])[3:]
            sums = re.findall("<span class=\"c2\">(.*?)</span>", self.lis[ii])
            heal = re.findall("<span class=\"c3\">(.*?)</span>", self.lis[ii])[1:]
            temp = re.findall("<span class=\"c4\">(.*?)</span>", self.lis[ii])[1:]
            date = temp[:len(temp) // 2]
            print(len(date))
            death = temp[len(temp) // 2:]
            df = DataFrame([date, diagnosis, sums, heal, death], ['日期', '确诊病例', '累积病例', '治愈病例', '死亡病例'])
            data[ii] = {}
            data[name] = df
            print('已爬取'+name+'的疫情信息')
            if not exists('./Data'):
                mkdir('Data')
            df.to_csv('./Data/' + name + '.csv', encoding='utf_8_sig')
        return data
                
if __name__ == '__main__':
    pass

