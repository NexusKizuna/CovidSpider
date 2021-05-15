import re
import requests as rq
from UserAgentPool import UserAgentPool
from time import sleep
from random import randint, random


class IpPool:
    def __init__(self):
        self.__ipPool = []
        self.__start()

    def __start(self):
        url = 'https://www.7yip.cn/free/?action=china&page='
        header = UserAgentPool()
        tempIpInformation = []
        for i in range(10):
            try:
                r = rq.get(url+str(i+1), headers=header.getUserAgent())
                r.encoding = 'utf-8'
                tempIpInformation.append(r.text)
            except:
                print('GetIpError')
            sleep(randint(1, 2) + random())

        for i in range(len(tempIpInformation)):
            checkhtml = tempIpInformation[i]
            ip = re.findall(r'<td data-title="IP">(.+?)</td>', checkhtml)
            port = re.findall(r'<td data-title="PORT">(.+?)</td>', checkhtml)
            later = re.findall(r'<td data-title="响应速度">(.+?)秒</td>', checkhtml)
            later = [float(later[i]) for i in range(len(later))]
            for j in range(len(later)):
                if later[j] < 5:
                    self.__ipPool.append('http:'+ip[j]+':'+port[j])
            del checkhtml, ip, later, port
        del tempIpInformation, header, url

    def getIp(self):  # 外部获取Ip方式
        return self.__ipPool[randint(0, len(self.__ipPool))]

    def popIp(self, breakIp):  # 返回无法爬取的Ip
        self.__ipPool.pop(breakIp)