from  selenium import webdriver
import time
import  re
path=r'D:\google\Chrome\Application\chromedriver.exe'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
#获取浏览器操作句柄和输入元素框
#对输入进行gbk编码
bro=webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
def  encod(con):
    res=con.encode('gb2312')
    res=str(res)
    res=re.sub(r'\\x','%',res)
    res=re.sub(r'b\'|\'','',res)
    return  res

def get_ele(data):
    #bro=webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
    bro.get('https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word='+data+'\n')
    #ele1=bro.find_element_by_id('kw')
    #ele1.send_keys(''+data+'\n')
    bro.maximize_window()
    ele2=bro.find_elements_by_class_name('ti')
    return  ele2#,bro
#对浏览器的元素进行操作
def  get_content(ele,i,bro):
    ele.click()
    allwin=bro.window_handles
    bro.switch_to_window(allwin[-1])
    try:
        ele3=bro.find_element_by_xpath('/html/body/div[4]/div/section/article/div[3]/div[2]/div[2]/div[1]')
        if(ele3):
            con=ele3.text
            con=re.sub(r'展开全部','',con)
            print('答案'+str(i)+'：')
            print(con)
            print('\n')
            bro.close()
            bro.switch_to_window(allwin[0])
    except Exception  as  e:
        bro.close()
        bro.switch_to_window(allwin[0])
        return

if __name__=="__main__":
    while 1:
        data=input('输入查询内容：')
        if(data):
            try:
                res=encod(data)
                ele2=get_ele(res)
                for i in range(5):
                    get_content(ele2[i],i,bro)
            except  Exception  as  e:
                print('请稍等....')

        
        
        

            
            

    

    
