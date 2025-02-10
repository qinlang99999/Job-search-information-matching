import pandas as pd
import matplotlib.pyplot as plt


#可视化绘制画像
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
    plt.savefig(f'../py_test/result__画像/企业画像/企业关于《{pa_name}》的画像.png',dpi=1000)
    plt.show()
    
test_1=pd.read_csv(r"../py_test/result2/test11-1.csv")
print(test_1.head())




###职位关键词汇总
state_dic={}
state=list(test_1['招聘岗位'])

for sta in state:
    if type(sta)==float:
        sta=[]
    else:
        sta=sta.strip('[')
        sta=sta.strip(']')
        sta=sta.split(',')
        for EP_n in range(len(sta)):
            sta[EP_n]=sta[EP_n].lstrip()
            sta[EP_n]=sta[EP_n].strip("'")
#    print(EP)

    for Sta in sta:
        if Sta not in list(state_dic):
            state_dic[Sta]=1
        else:
            state_dic[Sta]+=1
    
st_lis=list(state_dic)
for pre in st_lis:
    if state_dic[pre]<=5:
        if '零碎职业需求' not in list(state_dic):
            state_dic['零碎职业需求']=1
        else:
            state_dic['零碎职业需求']+=1
        del state_dic[pre]

print(state_dic)
Pre_del=state_dic['零碎职业需求']
del state_dic['零碎职业需求']
            
            
hist_pain(state_dic,'职位关键词统计',f'职位关键词\n剔除需求小于6的零碎职业：\n{Pre_del}人','人数')




#地区预处理
Work_GD=list(test_1['工作地点'])
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
hist_pain(WG_dic,'地区统计','省份','人数')
        
        
#工资薪水预处理
#sa_type={}
Sa_1=list(test_1['最高薪资'])
Sa_0=list(test_1['最低薪资'])
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



hist_pain(Sal_min,'最小工资统计','最小工资(值为10000的人最多)','人数')
hist_pain(Sal_max,'最大工资统计','最大工资(值为15000的人最多)','人数')


Ex_dic={}
Experience=list(test_1['经验要求'])

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
EducationD={0:'不限',1:'大专',2:'本科',3:'硕士',4:'博士',5:'技工'}
Education=list(test_1['学历要求'])
for Ed in Education:
    if type(Ed)==float:
        Education_dic['不限']+=1
    else:
        Education_dic[EducationD[Ed]]+=1
        
print("\n学历统计:")
print(Education_dic)
del Education_dic['不限']
hist_pain(Education_dic,'学历统计','学历条件','人数')



