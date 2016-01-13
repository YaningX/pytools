#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from bs4 import BeautifulSoup

__all__ = ['getPM25']
def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    html = urllib2.urlopen(site)
    soup = BeautifulSoup(html)
    city = soup.find(class_ = 'bi_loaction_city')
    aqi = soup.find("a",{"class","bi_aqiarea_num"})
    quality = soup.select(".bi_aqiarea_right span")
    result = soup.find("div",class_ ='bi_aqiarea_bottom')
    return  city.text + u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text


if __name__ == '__main__':
    getPM25('chengdu')