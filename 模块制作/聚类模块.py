from  sklearn.feature_extraction.text  import  TfidfTransformer  
from  sklearn.feature_extraction.text  import  CountVectorizer
from  sklearn.cluster import KMeans as  KM
import  pandas  as   pd
import  numpy  as  np
import  re
import  jieba
#进行分词制作
def cut(sen):
    str1=''
    word_list=jieba.lcut(sen)
    for word in word_list:
        str1=str1+word+' '
    return  str1
#读取语料库
def get_data():
    arr=[]
    with open('e:/1.txt','r',encoding='utf-8') as  f:
        for line in f:
            line=re.sub(r'\n|\ufeff','',line)
            arr.append(line)
    return  arr
t=[cut(s)  for s  in  get_data()]
#print(t)
CV=CountVectorizer(token_pattern='(?u)\\b\\w+\\b')
TF=TfidfTransformer()
ma=CV.fit_transform(t)
print(CV.get_feature_names())
ma1=TF.fit_transform(ma)
ma=ma.todense()
#print(ma)
#print(len(ma))
#print('\n')
#制作词频获取器
def get_WF(sen,wb=CV.get_feature_names()):
    arr=[]
    #arr1=[]
    for word in  wb:
        res=re.findall(r''+word+'',sen)
        lengh=len(res)
        arr.append(lengh)
    #arr1.append(arr)
    arr1=np.array(arr)
    return  arr1
def   get_tf(sen):
    c_ma=ma
    shi=get_WF(sen)
    new_ma=np.vstack([c_ma,shi])
    #print(new_ma)
    #print(len(new_ma))
    test=TF.fit_transform(new_ma)
    #print(test.todense())
    return  test[-1].todense()
class  train_pre():
    def __init__(self):
        self.ma1=TF.fit_transform(ma)
        self.model=KM(6)
        self.res=self.model.fit_predict(self.ma1)
    def  pre(self,mat):
        print(self.res)
        return  self.model.predict(mat)
    
#经行预测
#print(ma)
#print(len(ma))
#print('\n')
tf=get_tf('导航一下怎么去南昌')
print(tf)
print('\n')
#print(ma1[0].todense())
res=train_pre()
print(res.pre(tf))



    




