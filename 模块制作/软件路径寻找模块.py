import win32com.client
import  os
import  re
with open('e:/position_init/desktop_position.txt','r')  as  f:
    position=f.read()
    f.close()
position=position.split('\n')
def get_shortcuts():
    arr=[]
    for i in position:
        for root,dir1,file  in  os.walk(i):
            for m in  file:
                path=root+m
                arr.append(path)
    return arr
path=get_shortcuts()
def get_name():
    arr=[]
    for i in  path:
        result=i.split('/')
        name=result[-1]
        name=re.sub(r'\.lnk','',name)
        arr.append(name)
    return  arr
name=get_name()
def  corr():
    cor={name[i]:path[i] for i in  range(len(name))}
    return  cor
#下面这部分可以添加到主模块里面
cor=corr()
def  get_position(name):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(name)
    target=shortcut.TargetPath
    if(len(target)>5):
        return  target
if   __name__=='__main__':
    while 1:
        try:
            name=input('快捷方式名称：')
            name=cor[name]
            ab_path=get_position(name)
            print(ab_path)
        except  Exception  as  e:
            print('貌似没有这个快捷方式名称，或者你按住F5键刷新一下，或者这个不属于快捷方式QWQ')


