from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  os
chrome_driver=r'D:\google\Chrome\Application\chromedriver.exe'
def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=chrome_options)#,chrome_options=options)
    driver.get('https://map.baidu.com/dir/昭通/镇雄/@13030313.236263737,3472158.5,8.28z?querytype=walk&sn=2$$$$$$昭通&en=2$$$$$$镇雄$$$$$$&c=104&exptype=dep&version=5&route_traffic=3&mrs=1&da_src=shareurl')
    con=driver.find_elements_by_class_name('navtrans-navlist-list-content')
    ele=driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul[2]/li/div[1]/div/div/div[1]/div[2]/div/div/div[1]/p[1]')
    print('花费时间：')
    print(ele.text)
    print('\n')
    print('具体路线：')
    for i  in  con:
        print(i.text)
    driver.quit()
    
if __name__ == '__main__':
    main()

