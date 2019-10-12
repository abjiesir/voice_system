from  selenium import  webdriver
import time
import  os
chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
path=r'D:\google\Chrome\Application\chromedriver.exe'
br=webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
def trans(word):
    br.get('https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%BF%BB%E8%AF%91%E5%9C%A8%E7%BA%BF&rsv_pq=c94f5bf1000ec3cc&rsv_t=d5f6cZMTYuwlkntZdCOIsl0Mzbt1LLU0pXbP05znrVOykmIKHs3PTvT0eFk&rqlang=cn&rsv_enter=1&rsv_dl=ts_1&rsv_sug3=7&rsv_sug1=5&rsv_sug7=101&rsv_sug2=1&prefixsug=%25E7%25BF%25BB%25E8%25AF%2591&rsp=1&inputT=3563&rsv_sug4=4282')
    ele=br.find_element_by_xpath('//*[@id="1"]/div[1]/div[2]/form/div[1]/div/textarea')
    ele.send_keys(word)
    ele1=br.find_element_by_xpath('//*[@id="1"]/div[1]/div[2]/form/div[2]/div/a[2]').click()
    allwin=br.window_handles
    br.switch_to_window(allwin[-1])
    while 1:
        try:
            ele2=br.find_element_by_xpath('//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]')
            print(ele2.text)
            allwin=br.window_handles
            br.close()
            br.switch_to_window(allwin[0])
            break
        except  Exception  as  e:
            pass
if __name__=='__main__':
    while 1:
        word=input('输入翻译词：')
        trans(word)
