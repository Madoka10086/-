import numpy as np
import pandas as pd
import math

def delete_space(x):
    if type(x) is str:
        return x.strip()
    else:
        return x
#计算地区相对专业化指数
def RSI(df):
    df.set_index(["行业"], inplace=True)
    df = df.fillna(0)
    city = list(df)[0:10]
    industry = list(df.index)
    # print(city)
    # print(industry)
    rsi = []
    for i in city:
        k = 0
        for j in industry:
            s = int(df[i][j])/df[i].sum()
            mean = (df.loc[j].sum()-df[i][j])/(df.sum().sum()-df[i].sum())
            # print(df.loc[j].sum()-df[i][j])
            # print(df.sum().sum()-df[i].sum())
            # print(df[i][j])
            # print(df[i].sum())
            # print(s)
            k = k + abs(s-mean)
        rsi.append(k)
    return rsi

#计算制造业平均集中率
def MAR(df):
    df.set_index(["行业"], inplace=True)
    df = df.fillna(0)
    city = list(df)[0:10]
    industry = list(df.index)
    # print(city)
    # print(industry)
    mar = []
    for i in city:
        k = 0
        for j in industry:
            if df.loc[j].sum() != 0:
                v = int(df[i][j])/df.loc[j].sum()
            else:
                v = 0
            k = k + v
        mar.append(k/len(industry))
    return mar

#计算SP指数
def SP(df,distance):
    c = 0.0015
    df.set_index(["行业"], inplace=True)
    df = df.fillna(0)
    city = list(df)[0:10]
    industry = list(df.index)
    # print(city)
    # print(industry[7:35])
    sp = []
    for l in industry[7:35]:
        k = 0
        for i in city:
            for j in city:
                vi = int(df[i][l])/df[i][7:35].sum()
                vj = int(df[j][l])/df[j][7:35].sum()
                dij = distance[i][j]
                k = k + vi*vj*dij 
        sp.append(c*k)        
    return sp

#计算最高产值所属地区及其份额
def product(df):
    df.set_index(["行业"], inplace=True)
    df = df.fillna(0)
    city = list(df)[0:10]
    industry = list(df.index)
    pr = []

    for l in industry[7:35]:
        m = df.loc[l].max()
        p = round(m/df.loc[l].sum(),4)
        for i in city:
            if df[i][l] == m:
                c = i
                break
        pr.append(c+'('+str(p)+')')
    return pr

if __name__ == "__main__":
    city = ['广州','深圳','珠海','佛山','惠州','东莞','中山','江门','肇庆']
    industry = ['农副食品加工业', '食品制造业', '饮料制造业', '烟草制品业', '纺织业', '纺织服装、鞋、帽制造业', '皮革、毛皮、羽毛(绒)及其制品业', '木材加工及竹、藤、棕、草制品业', '家具制造业', '造纸及纸制品业', '印刷业和记录媒介的复制', '文教体育用品制造业', '石油加工、炼焦及核燃料加工业', '化学原料及化学制品制造业', '医药制造业', '化学纤维制造业', '橡胶制品业', '塑料制品业', '非金属矿物制品业', '黑色金属冶炼及压延加工业', '有色金属冶炼及压延加工业', '金属制品业', '通用设备制造业','专用设备制造业', '交通运输设备制造业', '电气机械及器材制造业', '通信设备、计算机及其他电子设备制造业', '仪器仪表及文化、办公用机械制造业', '工艺品及其他制造业']    
    industry = ['农副食品加工业', '食品制造业', '酒、饮料和精制茶制造业', '烟草制品业', '纺织业', '纺织服装、服饰业', '皮革、毛皮、羽毛及其制品和制鞋业', '木材加工和木、竹、藤、棕、草制品业', '家具制造业', '造纸和纸制品业', '印刷和记录媒介复制业', '文教、工美、体育和娱乐用品制造业', '石油加工、炼焦和核燃料加工业', '化学原料和化学制品制造业', '医药制造业', '化学纤维制造业', '橡胶和塑料制品业', '非金属矿物制品业', '黑色金属冶炼和压延加工业', '有色金属冶炼和压延加工业', '金属制品业', '通用设备制造业', '专用设备制造业', '汽车制造业', '铁路、船舶、航空航天和其他运输设备制造业', '电气机械和器材制造业', '计算机、通信和其他电子设备制造业', '仪器仪表制造业']    
    df2 = pd.DataFrame(columns=city)
    df3 = pd.DataFrame(index=industry)
    distance = pd.read_csv('距离.csv',encoding='utf-8')
    distance.set_index(["距离"], inplace=True)
    

    for filename in range(2011,2019):
        print(filename)
        df = pd.read_csv(str(filename)+'.csv',encoding = 'utf-8')
        df.applymap(delete_space)
        # rsi = RSI(df)#计算地区间相对专业化指数
        # df2.loc[str(filename)] = rsi


        # mar = MAR(df)#计算制造业平均集中率
        # df2.loc[str(filename)] = mar
        
        # sp = SP(df,distance)#计算SP指数
        # df3[str(filename)] = sp

        # pr = product(df)#计算最高产值
        # df3[str(filename)] = pr

        # print(df3)
        # print(df2)

    
    # df2.to_csv('地区间相对专业化指数.csv',encoding = 'gb2312')
    # df2.to_csv('地区平均产业集中率.csv',encoding='gb2312')
    # df3.to_csv('SP指数2003-2010.csv',encoding = 'gb2312')
    # df3.to_csv('最高产值及份额2003-2010.csv',encoding = 'gb2312')
    # df3.to_csv('SP指数2011-2018.csv',encoding = 'gb2312')
    # df3.to_csv('最高产值及份额2011-2018.csv',encoding = 'gb2312')
    



