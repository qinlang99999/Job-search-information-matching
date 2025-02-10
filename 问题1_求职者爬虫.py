from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import requests
import json
import time



edc={'不限':0,'技工':1,'大专':2,'本科':3,'硕士':4,'博士':5}
edcl=list(edc)
#r'py_test/result1/result1-2.csv'
f = open(r'C:\Users\Administrator\Desktop\result1-2.csv','w',encoding='UTF-8',newline='') 
csvwriter = csv.DictWriter(f, fieldnames=['ID',
                                          '姓名',
                                          '性别',
                                          '年龄',
                                          '个人简介',
                                          '工作经验',
                                          '期望职位',
                                          '工资薪水',
                                          '期望行业',
                                          '到岗时间',
                                          '工作地区',
                                          '关键词列表',
                                          '学历'
                                          ])
csvwriter.writeheader()



url='https://www.5iai.com/#/moreResume'
#新建浏览器driver

driver=webdriver.Chrome()
#1.打开网址
driver.get(url)
web = webdriver.Chrome() 
page_num=int(driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/div/div[2]/div[1]/div[2]/div/ul/li[8]').text)    
    
    
    


def info(n):
    
    def Get_id_user(GTN):#里面的数据表示需要爬取的页数
        ID_Data=[]
        for i in range(1,GTN+1):
            url=f'https://www.5iai.com/api/resume/baseInfo/public/es?pageSize=10&pageNumber={i}&function=&skills=&workplace=&keyword='          
            ID_Initial=requests.get(url)
            ID_Initial.encoding='utf-8'
            Dic_text=json.loads(ID_Initial.text) 
            for i in Dic_text['data']['content']:
                ID_Data.append(i['id'])
            
        return ID_Data
    
    user_id = Get_id_user(n)#输入页数
    
    
    website_list = []
    for ID in user_id :#网址列表
        url = f'https://www.5iai.com/#/moreResume/detail/{ID}'
        website_list.append(url)    




    #print("测试",lis1[0].find_element(By.CSS_SELECTOR ,'.position').text)
    username=[]
    expectPosition=[]
    keywordList=[]
    
    loop_num=len(website_list)
    print(loop_num)
    
    for i in range(n):
        if i!=n-1:
            m_num=11
        else:          
            m_num=(loop_num-(n-1)*10)+1
            print(loop_num)
            
        for num in range(1,m_num):
             #姓名
            username.append(driver.find_element(By.XPATH,f'//*[@id="app"]/div/section/section/div/div[2]/div[1]/ul/div[{num}]/li/div/div/div[1]/p[1]/span[1]').text)
            #期望职位
            expectPosition.append(driver.find_element(By.XPATH,f'//*[@id="app"]/div/section/section/div/div[2]/div[1]/ul/div[{num}]/li/div/div/div[1]/p[2]/span[1]').text)
            
        driver.find_element(By.CLASS_NAME,'btn-next').click()
        time.sleep(1)    
    
        
    
        
        
        
    for i in range(loop_num):
        ID = user_id[i]
        url = website_list[i]
        web.get(url)

        time.sleep(1)

        #姓名
        
                
        #性别
        try:
            gender = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[1]/div[2]/p[1]/span[1]').text
        except:
            gender =None
        #年龄
        try:
            age = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[1]/div[2]/p[1]/span[2]').text
        except:
            age =None
        
        #个人简介
        try:
            intro = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/p[2]').text
        except:
            intro =None
        #工作经验
        try:
            exp = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[1]/div[2]/p[1]/span[4]').text
        except:
            exp =None
        
        
        #工资薪水
        try:
            willSalary = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/p[1]').text
        except:
            willSalary =None
        
        #期望行业
        try:
            Expected_industry = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/p[2]/span[2]').text
        except:
            Expected_industry =None
        
        #到岗时间
        try:
            Time_of_arrival = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/p[3]/span[2]').text
        except:
            Time_of_arrival =None
        
        #工作地区
        try:
            city = web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div/div[1]/div[2]/p[1]/span[3]').text
        except:
            city =None
        #关键词列表
        try:
            keywordList=web.find_element(By.XPATH,'//*[@id="app"]/div/section/div/div[2]/div/div[1]/div[2]/div/div[2]').text
            
        except:
            keywordList=None
        
        #教育经历
        try:
           
            education=''
            edc=web.find_elements(By.CSS_SELECTOR,"[class='el-col el-col-12']")
          
            for ed in range(len(edc)-7):
                ed=edc[7+ed].text
                if ed in edcl:
                    education=ed       
            if education=='':
                education=None
            
        except:
            education=None

        
 
        adict = {'ID':ID,
                 '姓名':username[i],
                 '性别':gender,
                 '年龄':age,
                 '个人简介':intro,
                 '工作经验':exp,
                 '期望职位':expectPosition[i],
                 '工资薪水':willSalary,
                 '期望行业':Expected_industry,
                 '到岗时间':Time_of_arrival,
                 '工作地区':city,
                 '关键词列表':keywordList,
                 '学历':education
                 
                 }
        csvwriter.writerow(adict)
        #print(ID,username,gender,age,intro,exp,expectPosition,willSalary,Expected_industry,Time_of_arrival,city,keywordList)#,updateTime,skillMedalList
    
info(5)#page_num

driver.quit()
web.quit()

