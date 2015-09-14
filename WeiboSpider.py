# -*- coding: UTF-8 -*-
__author__ = 'starkshaw'

'''
WeiboSpider by Stark Shaw

'''

import sys

reload (sys)
sys.setdefaultencoding ('utf8')

import urllib2
from bs4 import BeautifulSoup

print '初始化……'
urlPrefix = 'http://m.weibo.cn/'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4'
examplePage = open('ex.html', 'w')
print '\n请注意\n本程序将会要求使用用户微博的 Cookie 数据，如果你继续使用本程序，则表示你同意上述请求。\n'

try:
    lines = [line.rstrip ('\n') for line in open ('cookie.txt')]
except IOError:
    print '无法找到 cookie.txt. 请创建一个文本文件并且命名为 cookie.txt 并且将你的 cookie 数据放在第一行中，然后再试一次。'
else:
    cookie = lines[0]
    print '你的用户信息如下：\nUser Agent: ' + user_agent
    #print '\nCookie: ' + cookie
    userID = raw_input ('\n需要追踪的用户 ID: ')
    url = urlPrefix + userID
    header = {'Connection': 'keep-alive',
              'cookie': cookie,
              'User-Agent': user_agent}
    request = urllib2.Request (url, headers = header)
    response = urllib2.urlopen (request)
    htmlStr = response.read()
    rawPage = BeautifulSoup (htmlStr, "html.parser")
    examplePage.write(unicode(rawPage))
    examplePage.close()
    title = rawPage.head.title.string
    if title == '微博':
        print 'ID 不存在。'
        quit()
    else:
        userInfo = rawPage.body.script.string
        nickname = userInfo.split(";")[1].split(",")[24][8:len(userInfo.split(";")[1].split(",")[24])-1].decode('unicode-escape').encode('utf-8')
        following = userInfo.split(";")[1].split(",")[16][10:len(userInfo.split(";")[1].split(",")[16])-1].decode('unicode-escape').encode('utf-8')
        followers = userInfo.split(";")[1].split(",")[19][11:len(userInfo.split(";")[1].split(",")[19])-1].decode('unicode-escape').encode('utf-8')
        location = userInfo.split(";")[1].split(",")[17][15:len(userInfo.split(";")[1].split(",")[17])-1].decode('unicode-escape').encode('utf-8')
        amountOfWeibo = userInfo.split(";")[1].split(",")[18][12:len(userInfo.split(";")[1].split(",")[18])-1].decode('unicode-escape').encode('utf-8')
        amoutOfFav = userInfo.split(";")[1].split(",")[22][20:len(userInfo.split(";")[1].split(",")[22])-1].decode('unicode-escape').encode('utf-8')
        timeOfReg = userInfo.split(";")[1].split(",")[27][14:len(userInfo.split(";")[1].split(",")[27])-1].decode('unicode-escape').encode('utf-8')
        print '\n昵称：' + nickname
        print '关注：' + following
        print '粉丝：' + followers
        print '所在地：' + location
        print '微博数量：' + amountOfWeibo
        print '收藏数量：' + amoutOfFav
        print '账户创建时间：' + timeOfReg
        quit()