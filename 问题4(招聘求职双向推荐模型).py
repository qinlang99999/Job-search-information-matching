import pandas as pd
import csv

df1=pd.read_csv(r"py_test/result3/result3-1.csv")
df2=pd.read_csv(r"py_test/result3/result3-2.csv")
df_num=pd.read_csv(r"py_test/result2/test11-1.csv")



df3=pd.merge(df1,df2, on=['求职者ID','招聘信息ID'])


def sumx(x):
    df_sx=df3[df3['招聘信息ID']==x]
    df_sx=len(df_sx)
    return df_sx
    
    
    
    
dic={x:sumx(x) for x in df3['招聘信息ID'].unique()}
far=[]
da=df3['招聘信息ID']
for i in list(df3['招聘信息ID']):
    far.append(dic[i])
    
    
df3['火热度']=far
df3 = df3.sort_values(by=['火热度','岗位匹配度', '求职者满意度'], ascending=[True,False,False])


#工作所需人数的动态记录
def get_x(x1):
    df_get=df_num[df_num['ID'] == x1]
    
    df_get=df_get['岗位人数']
    df_get=list(df_get)
    return df_get[0]
    
    
    
    
peo_num= {x:get_x(x) for x in df3['招聘信息ID'].unique()}


#求职者收到offer数记录
job = {x:False for x in df3['求职者ID'].unique()}



# 录取结果的存储
f = open(r'py_test/result4/result4.csv','w',encoding='UTF-8',newline='') 
csvwriter = csv.DictWriter(f, fieldnames=['招聘信息ID'
                                          ,'求职者ID'
                                          ,'岗位匹配度'
                                          ,'求职者满意度'                                          
                                          ])

csvwriter.writeheader()




#模拟录取过程
for row in df3.iterrows():
    index, data = row
    #判断是否已经约满
    if job[data['求职者ID']] or peo_num[data['招聘信息ID']] == 0:
        continue


    peo_num[data['招聘信息ID']] -= 1
    job[data['求职者ID']]=True
    adict = {
        '招聘信息ID':data['招聘信息ID']
             ,'求职者ID':data['求职者ID']
             ,'岗位匹配度':data['岗位匹配度']
             ,'求职者满意度': data['求职者满意度']                                        
                                  
         }
    csvwriter.writerow(adict)
    #判断全部约满
    if sum(peo_num.values()) == 0:
        break
