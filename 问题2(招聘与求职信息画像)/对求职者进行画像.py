
EducationD={'不限':0,'大专':1,'本科':2,'硕士':3,'博士':4,'技工':5}


import pandas as pd
import matplotlib.pyplot as plt

test_2=pd.read_csv(r"../py_test/result2/test12-2.csv")
print(test_2.head())

def hist_pain(bdic,pa_name,x_lable,y_lable,wid=9,lon=9):
    lis_x=list(bdic)
    lis_y=[]
    for k in lis_x:
        v=bdic[k]
        lis_y.append(v)
        
    plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False    # 解决中文显示问题

    plt.figure()
    plt.rc('font', size=14)#设置图中字号大小
    plt.figure(figsize=(wid,lon))#设置画布
    plt.pie(lis_y, labels=lis_x,pctdistance=0.9
            ,autopct='%.2f%%'
            ,textprops={'color':'black', 'size':10, 'weight':'bold'})  #绘制饼图，并显示3位整数一位小数
    plt.title(pa_name)#添加标题
    plt.xlabel(''.join([x_lable,'/',y_lable]))#添加横轴标签
    plt.legend()
    plt.savefig(f'../py_test/result__画像/求职者画像/求职者关于《{pa_name}》的画像.png',dpi=1000)
    plt.show()
    
    
    
    
    
    
#期望职位预处理
Expected_position=list(test_2['期望职位'])
EPl_dic={}

for EP in Expected_position:
    if type(EP)=='':
        EP=[""]
    else:
        EP=EP.strip('[')
        EP=EP.strip(']')
        EP=EP.split(',')
        for EP_n in range(len(EP)):
            EP[EP_n]=EP[EP_n].lstrip()
            EP[EP_n]=EP[EP_n].strip("'")
            
    EPl_len=len(EP)
    
    if EPl_len not in list(EPl_dic):
        EPl_dic[EPl_len]=1
    else:
        EPl_dic[EPl_len]+=1


        
        
        
        
EP_dic={}

#期望职位预处理
for EP in Expected_position:
    if type(EP)=='':
        EP=[""]
    else:
        EP=EP.strip('[')
        EP=EP.strip(']')
        EP=EP.split(',')
        for EP_n in range(len(EP)):
            EP[EP_n]=EP[EP_n].lstrip()
            EP[EP_n]=EP[EP_n].strip("'")
            
    for EP_i in EP:
        if EP_i not in list(EP_dic):
            EP_dic[EP_i]=1
        else:
            EP_dic[EP_i]+=1
print("\n职位信息：")
print(EP_dic)
print("\n每人期望职位数目：")
print(EPl_dic)
hist_pain(EPl_dic,'期望职位的统计数量','期望的职位','职位需求量')
hist_pain(EP_dic,'期望职位的具体统计','期望的职位','职位需求量',12)


#工资薪水预处理
#sa_type={}
Sa_1=list(test_2['最高薪资'])
Sa_0=list(test_2['最低薪资'])
Sal_max={}
Sal_min={}
#print(Salary)
for Sa in range(len(Sa_0)):
    Sa=[Sa_0[Sa],Sa_1[Sa]]
    

    if Sa[0]!='':#len(Sa)==2
        S1=int(Sa[1])
        S0=int(Sa[0])
    else:
        if -1 not in list(Sal_max):
            Sal_max[0]=1
            Sal_min[0]=1
        else:
            Sal_max[0]+=1
            Sal_min[0]+=1
        continue
    #最高薪水
    if S1 not in list(Sal_max):
        Sal_max[S1]=1
    else:
        Sal_max[S1]+=1
    
    #最低薪水
    if S0 not in list(Sal_min):
        Sal_min[S0]=1
    else:
        Sal_min[S0]+=1

print("\n最小工资信息：")        
print(Sal_min)

print('\n最大工资')
print(Sal_max)



hist_pain(Sal_min,'最小工资统计','最小工资(值为4000的人最多)','人数')
hist_pain(Sal_max,'最大工资统计','最大工资(值为6000的人最多)','人数')



#工作经验预处理
Ex_dic={}
Experience=list(test_2['工作经验'])

for Ex in Experience:
    if type(Ex)==float:
        Ex=0 
    if Ex not in list(Ex_dic):
        Ex_dic[Ex]=1
    else:
        Ex_dic[Ex]+=1

        
print('\n工作经验年限：')
print(Ex_dic)
del Ex_dic[0]
hist_pain(Ex_dic,'工作经验年限','工龄','人数')




#学历预处理
Education_dic={'不限':0,'大专':0,'本科':0,'硕士':0,'博士':0,'技工':0}
Education=list(test_2['学历'])
for Ed in Education:
    if type(Ed)==float:
        Education_dic['不限']+=1
    else:
        Education_dic[Ed]+=1
        
print("\n学历统计:")
print(Education_dic)
del Education_dic['不限']
hist_pain(Education_dic,'学历统计','学历条件','人数')


#地区预处理
Work_GD=list(test_2['工作地区'])
WG_dic={}
for GD in Work_GD:
    if type(GD)==float:
        GD="无"

    if GD not in list(WG_dic):
        WG_dic[GD]=1
    else:
        WG_dic[GD]+=1
print('地址统计')
print(WG_dic)
del WG_dic['[]']
hist_pain(WG_dic,'地区统计','省份','人数')




    