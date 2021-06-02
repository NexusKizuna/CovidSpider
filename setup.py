import sys
sys.path.append('./Pool/')
from spider import SecondSpider
from ShowDataonMap import ShowDataonMap

a = SecondSpider.SecondSpider()
data = a.start()
map = ShowDataonMap(data)
map.SetMap()
