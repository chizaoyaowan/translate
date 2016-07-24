import urllib.request
import urllib.parse
import json
import easygui as g
import sys


while True:
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    msg="请输入需要翻译的文本："
    title='翻译小工具'
    default=''
    trans=g.enterbox(msg,title,default)
    if trans=='':
        continue
    
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'


    data={}
    data['type']='AUTO'
    data['i']=trans
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_ENTER'
    data['typoResult']='true'
    data=urllib.parse.urlencode(data).encode('UTF-8')

    req=urllib.request.Request(url,data,head)

    response=urllib.request.urlopen(req)
    html=response.read().decode('UTF-8')

    fanyi=json.loads(html)
      if g.ccbox(fanyi['translateResult'][0][0]['tgt'],choices=('继续翻译','退出')):
        continue
    else:
        sys.exit(0)
    


