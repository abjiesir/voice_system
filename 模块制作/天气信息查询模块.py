import  requests as  req
from  xpinyin  import  Pinyin
import  re
class  weather_message():
    def __init__(self,word):
        self.p=Pinyin()
        self.word=word
    def  get_pinyin(self):
        pin=self.p.get_pinyin(u''+self.word+'','')
        return  pin
    def  get_html(self):
        t=[]
        w=[]
        te=[]
        pin=self.get_pinyin()
        url='https://www.tianqi.com/'+pin+'/'
        head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        res=req.get(url,headers=head)
        res.encoding='utf-8'
        text=res.text
        time=re.findall(r'<li><b>.*?</li>',text)
        wether=re.findall(r'(<li>[\u4E00-\u9FA5]*</li>)',text)
        tem=re.findall(r'<li><span>.*?</li',text)
        for  i in  time:
            a=re.sub(r'<li><b>|</b><span>|</span><img src=.*','',i)
            t.append(a)
        for  j in  wether[:7]:
            b=re.sub(r'<li>|</li>','',j)
            w.append(b)
        for  k in  tem:
            c=re.findall(r'\d+',k)
            te.append(c)
            
        return  t,w,te
    
if __name__=='__main__':
    while 1:
        city=input('请输入城市名称：')
        if(len(city)==0):
            print('请输入城市名称')
        else:
            mes=weather_message(city)
            t,w,te=mes.get_html()
            for i in range(len(t)):
                print(t[i]+':'+w[i]+'\n'+'最低气温：'+te[i][1]+'\n'+'最高气温：'+te[i][0])
           
    
    
    































    
    

