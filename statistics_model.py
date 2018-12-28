import pandas as pd 
#按营业部在龙虎榜上出现的频率进行排序，将结果保存到sort_exalter.csv 文件中
df=pd.read_csv('data_of_longhu.csv')
times=df['exalter'].groupby(df.exalter).count()
exalter=times.sort_values(ascending=False)
exalter.to_csv('sort_exalter.csv')
#打印出来出现频率大于200 的营业厅
t=exalter[exalter>200]
#在data_of_longhu.csv文件中找出这些营业厅今年的交易数据
index=list(t.index)
deal_detail=pd.DataFrame()
for i in index[1:]:#机构专用是个一整体的概念所以对与分析营业部的信息没有本质的有效信息
    s=df[df.exalter==i]
    deal_detail=deal_detail.append(s)
deal_detail
deal_detail.index=range(len(deal_detail))
del deal_detail['Unnamed: 0']
deal_detail.drop_duplicates(inplace=True)
deal_detail.to_csv('DealDetail.csv')
group=deal_detail.groupby(df.exalter)#group is a object

    


