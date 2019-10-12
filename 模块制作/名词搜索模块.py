import requests
import  re
import  os
def  find_person(name):
    kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    url='https://baike.baidu.com/item/'+name+''
    r = requests.get(url, headers = kv, allow_redirects=True)
    r.encoding='utf-8'
    print(r.status_code)
    res=r.text
    res=re.sub(r'\xa9','',res)
    #print(r.text)
    with  open('e:/person_chach/1.html','w',encoding='utf-8')   as   f:
        f.write(res)
if __name__=='__main__':
    while 1:
        name=input('名词：')
        find_person(name)
        os.startfile('e:/person_chach/1.html')
    

