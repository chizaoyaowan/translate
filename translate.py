import urllib.request
import urllib.parse
import json

while True:
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    trans=input("请输入要翻译的文本：")


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


    print("翻译结果： %s"%(fanyi['translateResult'][0][0]['tgt']))


