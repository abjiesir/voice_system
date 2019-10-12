import  os
def  do_shell(order):
    a=os.popen(order)
    print(a.read())
if __name__=='__main__':
    while 1:
        order=input('输入执行的命令：')
        do_shell(order)
    
