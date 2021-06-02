import requests as rq
import json
from time import sleep
from random import randint
from pandas import DataFrame
from Pool.IpPool import IpPool
from Pool.UserAgentPool import UserAgentPool


# 从QQ的接口获取疫情数据的爬虫


class SecondSpider:
    def __init__(self):
        self.url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province='
        self.lis = []
        self.province = ['新疆', '黑龙江', '吉林', '辽宁', '河北', '天津', '内蒙古', '北京',
                         '山东', '山西', '陕西', '宁夏', '甘肃', '青海', '西藏', '江苏', '河南',
                         '浙江', '上海', '安徽', '湖北', '重庆', '四川', '贵州', '湖南', '江西',
                         '福建', '广东', '广西', '云南', '台湾', '海南', '澳门', '香港']

    def start(self):
        ip = IpPool()  # 实例化ip池
        userAgent = UserAgentPool()  # 实例化user-agent池
        count = 0
        error = 0
        print('开始爬取', end='\n')
        while count < len(self.province):
            provinceName = self.province[count]
            nowIp = ip.getIp()  # 从ip池中获取代理ip
            print('现在爬取: '+provinceName, end='\n')
            try:
                data = rq.get(self.url+provinceName, headers=userAgent.getUserAgent(), proxies=nowIp)  # 爬取数据
                data_dic = json.loads(data.text)
                self.lis.append(data_dic)
                sleep(randint(3, 10))
                error = 0
            except:  # 爬取数据失败时，重新获取代理Ip并剔除原代理Ip
                ip.removeIp(nowIp)
                nowIp = ip.getIp()
                sleep(randint(5, 13))
                if error < 4:  # 若重复5次爬取都未成功，则放弃爬取该城市的数据
                    error += 1
                    count -= 1
                elif error == 4:
                    self.lis.append('')
                    error = 0

            count += 1

            del data_dic, data
        print('爬取完毕', end='\n')
        return self.getData()

    def getData(self):
        data = {}
        print('开始处理数据', end='\n')
        for elem in range(len(self.lis)):
            tempdata = self.lis[elem]['data']
            diagnosis = []  # 确诊病例
            heal = []  # 治愈病例
            death = []  # 死亡病例
            date = []  # 日期
            sums = []  # 累计病例
            for perday in tempdata:
                diagnosis.append(perday['confirm_add'])
                heal.append(perday['heal'])
                death.append(perday['dead'])
                sums.append(perday['confirm'])
                date.append(str(perday['year'])+str(perday['date']))
            df = DataFrame([date, diagnosis, sums, heal, death], ['日期', '确诊病例', '累积病例', '治愈病例', '死亡病例'])
            data[self.province[elem]] = df
        print('数据处理结束', end='\n')
        return data  # 返回了字典类型 {省份：数据,......}
