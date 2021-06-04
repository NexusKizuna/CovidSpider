from pyecharts.charts import Map
from pyecharts import options as opts
from os import system

# 疫情状况从地图展示


class ShowDataonMap:
    def __init__(self, dataDic):
        self.__country = list(dataDic.keys())
        self.__data = [(local, dataDic[local].iloc[1, 8]) for local in self.__country]

    def SetMap(self):
        tempList = [self.__data[i][1] for i in range(len(self.__data))]
        max = 0
        for num in tempList:
            if max >= int(num):
                continue
            else:
                max = int(num)
        map = Map()
        map.add('确诊', self.__data, 'china')
        map.set_global_opts(title_opts=opts.TitleOpts(title='China Map'),
                            visualmap_opts=opts.VisualMapOpts(
                            max_=max,
                            min_=0,
                            is_piecewise=True))
        map.render_notebook()
        map.render('./china.html')
        system(r'.\china.html')


if __name__ == '__main__':
    dic = {'安徽': 995}
    a = ShowDataonMap(dic)
    a.SetMap()

