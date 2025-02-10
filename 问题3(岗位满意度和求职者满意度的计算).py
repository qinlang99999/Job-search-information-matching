
import pandas as pd
import numpy as np

df1 = pd.read_csv("py_test/result2/test11-1.csv")
df2 = pd.read_csv("py_test/result2/test12-2.csv")



df2 = df2.fillna(0)
df2['学历'] = df2['学历'].replace('不限',0)#替换
df2['学历'] = df2['学历'].replace('大专',1)
df2['学历'] = df2['学历'].replace('本科',2)
df2['学历'] = df2['学历'].replace('硕士',3)
df2['学历'] = df2['学历'].replace('博士',4)
df2['学历'] = df2['学历'].replace('技工',5)

df1.rename(columns = {'ID':'招聘信息ID'},inplace=True)
df2.rename(columns = {'ID':'求职者ID'},inplace=True)
df2.rename(columns = {'最高薪资':'预期最高薪资'},inplace=True)
df2.rename(columns = {'最低薪资':'预期最低薪资'},inplace=True)
df2.rename(columns = {'最低薪资':'预期最低薪资'},inplace=True)

job_match = pd.merge(df1.assign(key=1), df2.assign(key=1), on='key').drop('key', axis=1)

# 求四列数据的最大值
max_value = max(job_match[['最低薪资','最高薪资','预期最低薪资','预期最高薪资']].max())
# 求四列数据的最小值
min_value = min(job_match[['最低薪资','最高薪资','预期最低薪资','预期最高薪资']].min())
# 将薪资归一化
def min_max_normalize(x):
    if min_value == max_value:
        return x
    return (x - min_value) / (max_value - min_value)
job_match['最低薪资'] = job_match['最低薪资'].apply(min_max_normalize)
job_match['最高薪资'] = job_match['最高薪资'].apply(min_max_normalize)
job_match['预期最低薪资'] = job_match['预期最低薪资'].apply(min_max_normalize)
job_match['预期最高薪资'] = job_match['预期最高薪资'].apply(min_max_normalize)

def calculate_match(row):
    edu = 0
    job1 = 0
    exp = 0
    sal = 0
    ecp = 0
    extra_edu = 0
    extra_exp = 0
    match_rato = 0
    
    if row['最低薪资'] > row['预期最高薪资'] or row['最高薪资'] < row['预期最低薪资']:
        sal = 0.0

    if row['预期最低薪资']<row['最低薪资']:
        sal += row['最低薪资']-row['预期最低薪资']
    if row['最高薪资'] > row['预期最高薪资']:
        sal += row['最高薪资']-row['预期最高薪资']

    # 判断岗位是否匹配，如果有一个岗位匹配则匹配度为1，否则为0
    for ec in row['期望行业'][1:-1].split(','):
        if ec in row['职位关键词'][1:-1].split(','):
           ecp = 1

    for job in row['期望职位'][1:-1].split(','):
        if job in row['招聘岗位'][1:-1].split(','):
           job1 = 1
           
    if row['学历要求'] <= row['学历']:
        edu = 1
        extra_edu =1+ 0.1*(row['学历']-row['学历要求'])
        
     
    if row['经验要求'] <= row['工作经验']:
        exp = 1
        extra_exp =1 + 0.1*(row['工作经验']-row['经验要求'])
    #匹配度 = 【学历 * 0.3 * 额外权值  + 经验 * 0.3 * 额外权值 + 薪资 *0.3 +行业 * 0.1】* 岗位
    a = float(edu) * 0.3 * extra_edu + float(exp) * 0.3 * extra_exp +float(sal) * 0.3 + float(ecp) * 0.1
    match_rato  =  a * float(job1)
    match_rato = round(match_rato,2)
    if match_rato < 0.1:
        match_rato = 0
    return match_rato
    
    
# 计算岗位匹配度

job_match['岗位匹配度'] = job_match.apply(calculate_match, axis=1)
job_match['岗位匹配度'] = job_match['岗位匹配度'].replace(0,np.nan)
job_match = job_match.dropna()
job_match = job_match.sort_values(by='岗位匹配度', ascending=False)
# 根据匹配度降序排序

# 保存结果
job_match[['招聘信息ID', '求职者ID', '岗位匹配度']].to_csv('py_test/result3/result3-1.csv', index=False)


def calculate_satisfaction(row):
    # 判断薪资是否满意，如果不满意则满意度为0
    area = 0
    salary = 0
    job2 = 0
    edu = 0
    exp = 0
    extra_edu = 0
    extra_exp = 0
    sat_rato = 0
    if row['最低薪资'] < row['预期最低薪资'] or row['最高薪资'] < row['预期最高薪资']:
        salary = 0
    if row['最低薪资']>row['预期最低薪资']:
        salary += row['最低薪资']-row['预期最低薪资']
    if row['最高薪资'] > row['预期最高薪资']:
        salary += row['最高薪资']-row['预期最高薪资']
    
    for job in row['招聘岗位'][1:-1].split(','):
        if job in row['期望职位'][1:-1].split(','):
           job2 = 1
    
    for ar in row['工作地点'][1:-1].split(','):
        if ar in row['工作地区'][1:-1].split(','):
           area = 1
    
    if row['学历要求'] <= row['学历']:
        edu = 1
        extra_edu =1+ 0.1*(row['学历']-row['学历要求'])
    
    if row['经验要求'] <= row['工作经验']:
        exp = 1
        extra_exp =1 + 0.1*(row['工作经验']-row['经验要求'])
    
    #满意度 = 【学历 * 0.1 * 额外权值  + 经验 * 0.1 * 额外权值 + 薪资 *0.4 +行业 * 0.4】* 岗位
    b = float(edu) * 0.1 * extra_edu + float(exp) * 0.1 * extra_exp +float(salary) * 0.4 + float(area) * 0.4
    sat_rato  =  b * float(job2)
    sat_rato = round(sat_rato,2)
    if sat_rato < 0.1:
        sat_rato = 0
    return sat_rato 




# 计算满意度
job_match['求职者满意度'] = job_match.apply(calculate_satisfaction, axis=1)
job_match['求职者满意度'] = job_match['求职者满意度'].replace(0,np.nan)
job_match = job_match.dropna()
job_match = job_match.sort_values(by='求职者满意度', ascending=False)
# 保存结果
job_match.rename(columns = {'企业名称':'公司名称'},inplace=True)
job_match[['求职者ID','招聘信息ID', '求职者满意度','公司名称']].to_csv('py_test/result3/result3-2.csv', index=False)
print("ok ")






