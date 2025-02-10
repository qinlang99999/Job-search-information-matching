from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import requests
import json
import time

f = open(r'py_test/result1/result1-1.csv','w',encoding='UTF-8',newline='') 
csvwriter = csv.DictWriter(f, fieldnames=['ID',
                                          '企业名称',
                                          '招聘岗位',
                                          '薪资',
                                          '学历要求',
                                          '经验要求',
                                          '岗位人数',
                                          '公司类型',
                                          '职位关键词',
                                          '职位描述',
                                          '职位福利',
                                          '工作地点'
                                          ])
csvwriter.writeheader()




url='https://www.5iai.com/#/jobList'
#新建浏览器driver

driver=webdriver.Chrome()
#1.打开网址
driver.get(url)
web = webdriver.Chrome()
page_num=int(driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/div/div/ul/li[8]').text)









def info(n):#爬取函数
    def Get_id_job(GI_num):#里面的数据表示需要爬取的页数
        ID_Data=[]
        for i in range(1,GI_num+1):
            url=f'https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber={i}&willNature=&function=&wageList=%255B%255D&workplace=&keyword='          
            ID_Initial=requests.get(url)
            ID_Initial.encoding='utf-8'
            Dic_text=json.loads(ID_Initial.text) 
            for i in Dic_text['data']['content']:
                ID_Data.append(i['id'])
        return ID_Data


    name = []
    qualification = []
    datePay=[]
    experience =[]
    number =[]
    company_name = []
    company_type = []
    website_list = []
    
    job_id = Get_id_job(n)
    
    for ID in job_id :#网址列表
        url = f'https://www.5iai.com/#/jobDetails/{ID}'
        website_list.append(url)


    loop_num=len(website_list)
    print(loop_num)
    
    
    #主页面信息的爬取 ps： driver是必须的，不用就无法寻址
    for i in range(n):
        if i!=n-1:
            m_num=11
        else:          
            m_num=(loop_num-(n-1)*10)+1
            
        for num in range(1,m_num):
            name.append(driver.find_element(By.XPATH ,f"//*[@id='app']/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[1]/h5/span[1]").text)
            datePay.append(driver.find_element(By.XPATH ,f'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[1]/h5/span[2]').text)
            qualification.append(driver.find_element(By.XPATH ,f'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[1]/div/span[1]').text)
            experience.append(driver.find_element(By.XPATH ,f'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[1]/div/span[2]').text)
            number.append(driver.find_element(By.XPATH ,f'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[1]/div/span[3]').text)
            company_name.append(driver.find_element(By.XPATH ,f'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[2]/h5').text)
            company_type.append(driver.find_element(By.XPATH ,f'//*[@id="app"]/div/section/section/div/div[2]/div[2]/div[1]/ul/div[{num}]/li/div[1]/div[2]/div/span[2]').text)
        driver.find_element(By.CLASS_NAME,'btn-next').click()
        time.sleep(1)    
    

    
    #详情页面信息的爬取 ps：因为有新建web，所以需要分开循环
    for i in range(loop_num):
        ID = job_id[i]
        url = website_list[i]
        web.get(url)
        time.sleep(1)
        try:
            job_keyword = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[2]').text
        except:
            job_keyword=None
            
        try:
            job_descripition = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[6]').text
        except:
            job_descripition=None
        
        try:
            job_benefit = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[8]').text
        except:
            job_benefit = None
        try:
            job_place = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[10]').text
        except:
            job_place =None
        
        
        
        

        
        
 
        adict = {'ID':ID,
                 '企业名称':company_name[i],
                 '招聘岗位':name[i],
                 '薪资':datePay[i],
                 '学历要求':qualification[i],
                 '经验要求':experience[i],
                 '岗位人数':number[i],
                 '公司类型':company_type[i],
                 '职位关键词':job_keyword,
                 '职位描述':job_descripition,
                 '职位福利':job_benefit,
                 '工作地点':job_place
                 }

        csvwriter.writerow(adict)

    
info(5)#只需要调整这里面的数，就可以调整爬取的页数page_num
driver.quit()
web.quit()