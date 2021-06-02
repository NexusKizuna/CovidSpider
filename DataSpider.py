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
        self.id = {439: '湖北', 440: '浙江', 441: '广东', 442: '河南', 443: '湖南', 444: '安徽',
                   445: '重庆', 446: '江西', 447: '山东', 448: '四川', 449: '江苏', 450: '北京',
                   451: '上海', 452: '福建', 453: '广西', 454: '云南', 455: '陕西', 456: '河北',
                   457: '海南', 458: '黑龙江', 459: '辽宁', 460: '山西', 461: '天津', 462: '甘肃',
                   463: '内蒙古', 464: '宁夏', 465: '新疆', 466: '吉林', 467: '贵州', 468: '香港',
                   469: '台湾', 470: '青海', 471: '澳门', 472: '西藏'}

    def start(self):
        header = UserAgentPool()
        proxy = IpPool()
        i = 0
        idList = list(self.id.keys())
        while i < len(self.id):
            ip = ''
            try:
                ip = proxy.getIp()
                r = rq.get(self.url + idList[i] + '&s1=0&s2=0',
                           headers=header.getUserAgent(), proxies=ip)
                r.encoding = 'utf-8'
                self.lis.append(r.text)
                sleep(randint(2, 5) + random())
            except:
                proxy.removeIp(ip)
                sleep(randint(3, 10))
                i = i-1
            i += 1

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
            data[name] = df
            print('已爬取'+name+'的疫情信息')
            if not exists('./Data'):
                mkdir('Data')
            df.to_csv('./Data/' + name + '.csv', encoding='utf_8_sig')
        return data


if __name__ == '__main__':
    pass

