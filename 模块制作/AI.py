import   pyaudio
import   wave
import  os
from  aip  import  AipSpeech
import  re
import  random
import  sys
import  numpy  as  np
import  time
arr=['unknowned','unknowned','unknown，unknown']
ojb={'下午好':'先生，下午好','再见':'再见，先生，程序已经退出','自学习':'我还没有这个功能','完善你的资料库':'谢谢先生','男子':'先生请讲','你好':'你好','吃饭':'你吃吧，我不饿的','你叫什么':'我是可爱的楠梓小姐','爱你':'可惜我没有感情','喜欢':'反正我喜欢杰哥','多大':'我今年四岁了','你是谁':'我是可爱的楠梓小姐','能做什么':'我能查阅资料','女朋友':'我现在还没有感情这个东西','无聊':'你还有我呢'}
list1=[]
for  key,value  in  ojb.items():
    list1.append(key)
class  get_out_voice():
    def  __init__(self):
        self.CHUNK=1024
        self.FORMAT=pyaudio.paInt16
        self.CHANNELS=1
        self.RATE=16000
        self.TIME=1
        self.p=pyaudio.PyAudio()
        self.frames=[]
    def  get_stream(self):
        stream=self.p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)        
        #for  i  in  range(0,int(self.RATE/self.CHUNK*self.TIME)):
        c=32
        while c>0:
            #print(i)
            data=stream.read(self.CHUNK)
            audio_data = np.fromstring(data, dtype=np.short)
            #print(len(audio_data))
            #if((np.sum(audio_data>400))>350):
            #print(audio_data)
            print(np.mean(audio_data))
            self.frames.append(audio_data)
            c=c-1
                #break
            #c=c-1
        #e=time.time()
        #print(e-s)
                
        #print(self.frames)
        print('询问完毕')
        stream.stop_stream()
        stream.close()
        self.p.terminate()
    def  get_wav(self):
        wf=wave.open('e:/AI/2.wav','wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
class   translate():
    def  __init__(self):
        self.path='path'
        self.path1='path1'
        self.app_id='15657381'
        self.aip_key='0dALsaRkEmbl6rtg7zj0lecG'
        self.secret_key='PItZMGwUpCB2ye8xiS2Y5ehnTGxXmmMu'
        self.client=AipSpeech(self.app_id,self.aip_key,self.secret_key)
    def  tran(self,path,path1):
        str1='ffmpeg  -y   -i  '+str(path)+' -acodec  pcm_s16le  -f  s16le -ac  1 -ar  16000  '+str(path1)+''
        os.system(str1)
        with  open(path1,'rb') as  f:
            con=f.read()
            #print('yes')
        return  con
    def   say(self):
        content=self.tran('e:/AI/2.pcm','e:/AI/2.wav')
        content1=self.client.asr(content,'pcm',16000,{
        'dev_pid':1536,
        })
        #print(content1)
        list2=[]
        bool2=True
        for  key2,value2  in  content1.items():
            list2.append(key2)
        if('result' in  list2):
            bool2=False
            print(content1['result'][0])
            f_con=content1['result'][0]
            #return  content1['result'][0]
        else:#(bool2):
            result1=self.client.synthesis('unknowned','zh',1,{
            'vol':5,
            'spe':2,
            'pit':9,
            'per':4
            })
            with  open('e:/AI/3.wav','wb')  as  f:
                f.write(result1)
            os.startfile('e:/AI/3.wav')
        bool1=True
        for  i  in  range(len(list1)):
            re1=re.search(''+list1[i]+'',f_con)
            if(re1):
                if(re1.group()=='再见'):
                    result1=self.client.synthesis(ojb[list1[i]],'zh',1,{
                    'vol':5,
                    'spe':2,
                    'pit':9,
                    'per':4
                    })
                    with  open('e:/AI/3.wav','wb')  as  f:
                        f.write(result1)
                    os.startfile('e:/AI/3.wav')
                    sys.exit(0)
                else:
                    result1=self.client.synthesis(ojb[list1[i]],'zh',1,{
                    'vol':5,
                    'spe':2,
                    'pit':9,
                    'per':4
                    })
                    with  open('e:/AI/3.wav','wb')  as  f:
                        f.write(result1)
                    os.startfile('e:/AI/3.wav')
                    bool1=False
                    return 
        if(bool1):
            result1=self.client.synthesis(random.choice(arr),'zh',1,{
            'vol':5,
            'spe':2,
            'pit':9,
            'per':4
            })
            with  open('e:/AI/3.wav','wb')  as  f:
                f.write(result1)
            os.startfile('e:/AI/3.wav')
                
while  True:
    ju=input('开始询问吗：')
    if(str(ju)=='是'):
        try:
            a=get_out_voice()
            b=translate()
            a.get_stream()
            s=time.time()
            a.get_wav()
            b.say()
            #b.relay()
            e=time.time()
            print(e-s)
        except  Exception  as  e:
            print(e)
            
        
    

            
