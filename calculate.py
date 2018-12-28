# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 21:32:23 2018

@author: Administrator
"""
import pandas as pd
names=['李曜明','郭','关','吴']
def calculate(names):
    n=len(names)
    primal_capital=[20]*n
    df=pd.DataFrame(primal_capital).T
    df.columns = names
    while 1:
        x=[]
        for i in range(n):
            t=input()
            if t=='end':
                return  df
            else:
                t=int(t)
                x.append(t)
        x=pd.DataFrame(x).T
        x.columns= names
        df=df.append(x)
        #df.index(range(len(df)))
        print(df)
df=calculate(names)
df.sum()
        

