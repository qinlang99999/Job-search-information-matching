
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



df1 = pd.read_csv(r"py_test/result1/result1-1.csv")
#对于粗略地区的精确锁定省份，运用爬虫技术
def index_search(dr_i):
    url='https://ditu.so.com/'
    driver.get(url)
    time.sleep(1)
    input_element=driver.find_element(By.XPATH,'//*[@id="searchInputContainer"]/div[2]/input')   #获取该输入框的Xpath
    input_element.send_keys(dr_i)     # 向该输入框中
    buttob_element=driver.find_element(By.XPATH,'//*[@id="searchInputContainer"]/div[1]/div[2]') #获取该搜索按钮的位置
    #print(buttob_element.text)   打印该元素下的文本
    buttob_element.click()    # 点击完成跳转//*[@id="e_map_idea"]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]
    time.sleep(1)
    DZ=driver.find_element(By.XPATH,'//*[@id="menuBar1"]/div/div/a/span')   #获取该输入框的Xpath
    DZ=DZ.text[:2]
    try:
        te=driver.find_element(By.XPATH,'//*[@id="e_map_idea"]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div/div/div/div[1]/div/span/div/div[1]/div[1]/p[1]n')
        if len(dr_i)!=2:
            return index_search(dr_i[:2])
        else:
            return '无'
    except:
        if DZ in province:
            return DZ
        else:
            url='https://ditu.so.com/'
            driver.get(url)
            time.sleep(1)
            input_element=driver.find_element(By.XPATH,'//*[@id="searchInputContainer"]/div[2]/input')   #获取该输入框的Xpath
            input_element.send_keys(DZ)     # 向该输入框中输入
            buttob_element=driver.find_element(By.XPATH,'//*[@id="searchInputContainer"]/div[1]/div[2]')
            #print(buttob_element.text)   打印该元素下的文本
            buttob_element.click()    # 点击完成跳转
            time.sleep(1)
            DZ=driver.find_element(By.XPATH,'//*[@id="e_map_idea"]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/h5/span')
            DZ=DZ.text[:2]
            return DZ
        
province=["河北",'山西','辽宁','吉林','黑龙江',
          '江苏','浙江','安徽','福建','江西',
          '山东','河南','湖北','湖南','广东',
          '海南','四川','贵州','云南','陕西',
          '甘肃','青海','台湾','内蒙','广西',
          '西藏','宁夏','新疆','北京','天津',
          '上海','重庆']
SH={'广州':'广东','深圳':'广东','福州':'福建'}
SHL=list(SH)



df1.drop(['公司类型','职位福利','职位描述'], axis=1, inplace=True)
education1={'不限':0,'大专':1,'本科':2,'硕士':3,'博士':4,'技工':5}
experence ={'不限': 0, '1': 1, '1-3年': 2, '3': 3,  '3-5年': 4, '5': 5, '5-7年': 6, '7-10年': 7,  '10': 10}


df1 = df1.drop_duplicates(subset=['ID'])#ID去重


df1['学历要求'] = df1['学历要求'].replace('不限',0)#替换
df1['学历要求'] = df1['学历要求'].replace('大专',1)
df1['学历要求'] = df1['学历要求'].replace('本科',2)
df1['学历要求'] = df1['学历要求'].replace('硕士',3)
df1['学历要求'] = df1['学历要求'].replace('博士',4)
df1['学历要求'] = df1['学历要求'].replace('技工',5)

df1['经验要求'] = df1['经验要求'].replace('0',0)
df1['经验要求'] = df1['经验要求'].replace('经验不限',0)
df1['经验要求'] = df1['经验要求'].replace('不限',0)
df1['经验要求'] = df1['经验要求'].replace('1',1)
df1['经验要求'] = df1['经验要求'].replace('1-3年',2)
df1['经验要求'] = df1['经验要求'].replace('3',3)
df1['经验要求'] = df1['经验要求'].replace('3-5年',4)
df1['经验要求'] = df1['经验要求'].replace('5',5)
df1['经验要求'] = df1['经验要求'].replace('5-7年',6)
df1['经验要求'] = df1['经验要求'].replace('5-10年',6)
df1['经验要求'] = df1['经验要求'].replace('7年以上',7)
df1['经验要求'] = df1['经验要求'].replace('10',10)
df1['工作地点'] = df1['工作地点'].replace(' 广州大学城(大学城北)创智园3栋4楼','广州')
#后面处理时将用平均值代替不限
df1['岗位人数'] = df1['岗位人数'].replace('不限','0人')
df1['岗位人数'] = df1['岗位人数'].replace('人数不限','0人')



df1 = df1.dropna()
df1.loc[312,'薪资'] = '4.5-4.5'
df1.loc[318,'薪资'] = '3-4.5'
df1.loc[351,'薪资'] = '4.5-6'
df1.loc[352,'薪资'] = '3-3'


#招聘职位预处理
job_recruit = []
recruit_data=df1['招聘岗位'].tolist()
for EP in recruit_data:
    if type(EP)==float:
        EP=[]
    else:
        EP=EP.split('/')
#    print(EP)
    EPl_len=len(EP)
    job_recruit.append(EP)
    
df1['招聘岗位'] = job_recruit

alist = df1['薪资'].tolist()
blist = df1['岗位人数'].tolist()
for i in range(len(blist)):
    if type(blist[i])==float:
       blist[i]='0人' 
        

#职位关键词预处理
keyword = []
key=df1['职位关键词'].tolist()
for EP in key:
    if type(EP)==float:
        EP=[]
    else:
        EP=EP.split()
#    print(EP)
    EPl_len=len(EP)
    keyword.append(EP)

df1['职位关键词']=keyword   


#工作地点预处理
###地区预处理
Work_GD=list(df1['工作地点'])
WG_dic={}
#粗略提取地区数据
for GD in Work_GD:
    if type(GD)==float:
        GD=""
    else:
        GD=GD.lstrip()
        for PRO in province:
                if PRO in GD:
                    GD=PRO
                    break
        for PRO in SHL:
                if PRO in GD:
                    GD=SH[PRO]
                    break
                
    if GD not in list(WG_dic):
        WG_dic[GD]=1
    else:
        WG_dic[GD]+=1
        

dr_dic={}
driver=webdriver.Chrome()
for di in list(WG_dic):
    if len(di)>2:       
        dr_dic[di]=index_search(di)[:2]

#dr_dic对于很粗略的地址做出了解释

       
driver.quit()        


#               精确划分地区数据
area = []
upda_drl=list(dr_dic)
WG_dic={}

for GD in Work_GD:
    
    if type(GD)==float:
        GD=""
    else:
        GD=GD.lstrip()
        if GD in upda_drl:
            GD=dr_dic[GD]
        for PRO in province:
                if PRO in GD:
                    GD=PRO
                    break
        for PRO in SHL:
                if PRO in GD:
                    GD=SH[PRO]
                    break
    area.append(GD)
df1['工作地点'] = area


list1 = []
list2 = []
list3 = []
list4 = []

for item in alist:
    split_item = item.split("-")
    list1.append(split_item[0])
    list2.append(split_item[1])


    
for item in list2:
    split_item = item.split("K")
    list3.append(split_item[0])
    
Le_list4=0
for item in blist:
    split_item = item.split("人")
    list4.append(int((split_item[0])))
    if list4[-1]!=0:
        Le_list4+=1
#用平均值代替不限
E_peo=int(sum(list4)/Le_list4)
for item in range(len(list4)):
    if list4[item]==0:
        list4[item]=E_peo
    
list1 = [float(x)*1000 for x in list1]
list3 = [float(x)*1000 for x in list3]

df1.loc[:,'最低薪资'] = list1
df1.loc[:,'最高薪资'] = list3
df1['岗位人数'] = list4
df1.drop(['薪资'], axis=1, inplace=True)

df1['工作地点'] = df1['工作地点'].replace('.',None)
df1 = df1.dropna()

df1.to_csv(r"py_test/result2/test11-1.csv", index=False)




#employee预处理
df2 = pd.read_csv(r"py_test/result1/result1-2.csv")

df2 = df2.drop_duplicates(subset=['ID'])

#这里我觉得可以不舍弃不限
df2['期望行业']= df2['期望行业'].fillna('不限')
df2.drop([0])

list5 = []

list6 = []

clist = df2['工资薪水'].tolist()
for item in clist:
    split_item =item.split('-')
    if split_item[0]!='':        
        list5.append(split_item[0])
        split_item = split_item[1].split("元")
        
        list6.append(split_item[0])
    else:
        list5.append('0')
        list6.append('999999')

    
list5 = [float(x) for x in list5]
list6 = [float(x) for x in list6]

df2.loc[:,'最低薪资'] = list5
df2.loc[:,'最高薪资'] = list6

Ex_dic={}
seeker_experence = []
exdata=df2['工作经验'].tolist()

for Ex in exdata:
    if type(Ex)==float:
        Ex=0
    elif Ex[0]=='无':
        Ex=0
    else:
        Ex=int(Ex.split('年')[0])
    seeker_experence.append(Ex)
    
    if Ex not in list(Ex_dic):
        Ex_dic[Ex]=1
    else:
        Ex_dic[Ex]+=1


#期望职位预处理
joblist = []
Expected_position=df2['期望职位'].tolist()
for EP in Expected_position:
    if type(EP)==float:
        EP=[]
    else:
        EP=EP.split()
#    print(EP)
    EPl_len=len(EP)
    joblist.append(EP)


#期望行业预处理
jobtype = []
Expected_position=df2['期望行业'].tolist()
for EP in Expected_position:
    if type(EP)==float:
        EP=[]
    else:
        EP=EP.split('/')
#    print(EP)
    EPl_len=len(EP)
    jobtype.append(EP)


df2['工作经验'] = seeker_experence
df2['期望职位'] = joblist
df2['期望行业'] = jobtype

#期望工作地点预处理
area = []
area_set=df2['工作地区'].tolist()
for EP in area_set:
    if type(EP)==float:
        EP=[]
    else:
        EP=EP[0:2]
        EP=EP.split()
#    print(EP)
    EPl_len=len(EP)
    area.append(EP)

df2['工作地区'] = area
df2.drop(['个人简介','到岗时间','关键词列表','年龄','性别','姓名','工资薪水'], axis=1, inplace=True)
df2.to_csv(r"py_test/result2/test12-2.csv", index=False)







