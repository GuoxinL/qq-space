# -*- coding: utf-8 -*-
import json
import random
import sys
import urllib2

reload(sys)
sys.setdefaultencoding('utf8')
#
#       获得qq空间接口，个人空间信息数据
#

# 获得随机QQ号
def randomQQNumber():
    return 999999 + random.randint(1, 999999)


# 获得URL
# python 不能自动转换，使用 str(int)将数字转换成字符串
# return [u'http://qlogo1.store.qq.com/qzone/1943608/1943608/100', 30, -1, 0, 0, 0, u'\u4e1d\u74dc\u67a3\u7530', 0]
# 0 url
# 1 空间积分
# 2 黄钻积分，如果不是黄钻则是-1
# 3 黄钻等级
# 4 未知
# 5 未知
# 6 昵称
# 7 不是黄钻用户是0，是黄钻用户是1
def getUrl(number):
    return 'http://r.pengyou.com/fcg-bin/cgi_get_portrait.fcg?uins=' + str(number)


# 转换返回数据为json对象
# str.index(str) 在str中寻找指定字符串的下标
# json.loads(str) 将字符串转换成json对象
# json.dumps()把一个Python对象编码转换成Json字符串
def getJsonObject(str):
    befor = str.index('(')
    end = str.index(')')
    # print befor
    # print end
    jsonString = data[befor + 1:end]
    jsonObject = json.loads(jsonString)
    return jsonObject



number = randomQQNumber()
response = urllib2.urlopen(getUrl(number))
data = response.read().decode("GBK").encode("UTF-8")
jsonObject = getJsonObject(data)
qq = jsonObject.keys()
print qq
print "输出qq"
print qq[0]
infoArray = jsonObject[qq[0]]
print "输出infoArray"
print infoArray
for info in infoArray:
    print "输入info"
    print info
