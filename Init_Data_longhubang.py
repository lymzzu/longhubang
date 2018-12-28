import datetime 
import tushare as ts 
import pymysql 
import pandas as pd 
import numpy as np 
import time
#生成一个交易时间段，给定start_dt,end_dt
def date_seq(start_dt,end_dt):
    date_series=pro.trade_cal(exchange_id='', is_open=1, start_date= start_dt, end_date=end_dt )
    date_temp = list(date_series.iloc[:, 1])
    date_seq = [(datetime.datetime.strptime(x, "%Y%m%d")).strftime('%Y%m%d') for x in date_temp]
    #print(date_seq)
    return date_seq

if __name__ == "__main__":
    #设置tushare pro 的token 并连接
    ts.set_token('f57dbc00c114806dc5572773fe2598fd70f6cdcb019f230d1a88ea23')
    pro = ts.pro_api('f57dbc00c114806dc5572773fe2598fd70f6cdcb019f230d1a88ea23')
    #设定获取日线行情的初始日期和终止日期
    start_dt='20180101'
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y%m%d')
    #调用date_seq函数得到交易时间段
    date_time=date_seq(start_dt,end_dt)
    #提取数据
    df=pd.DataFrame()
    t0=datetime.datetime.now()
    i=1
    for date in date_time:
        t = pro.top_inst(trade_date=date)
        i+=1
        t1=datetime.datetime.now()
        df=df.append(t)
        #由于接口限制这能60秒访问60次，所以写了一个当一分钟内访问60次以后暂停程序几秒
        if i%60==0 and t1-t0< datetime.timedelta(seconds=60):
            time.sleep((datetime.timedelta(seconds=60)-(t1-t0)).seconds+1)
            t0=datetime.datetime.now()
        print('ok'+date)
    print(df)
df.to_csv('data_of_longhu.csv')

    



