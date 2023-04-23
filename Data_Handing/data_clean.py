from pandas import DataFrame
import pandas as pd


"""
    判断空值：isnull()
"""
def na_determine():
    miss_value = ['n/a','na','--']  #为空值的判断条件值
    df = pd.read_csv("property-data.csv", na_values=miss_value)
    print(df['NUM_BEDROOMS'])
    print(df['NUM_BEDROOMS'].isnull())  #isnull判断单元格是否为空 True：为空 | False：不为空


"""
    移除空值的行：inplace=True
"""
def delete_data():
    df = pd.read_csv("property-data.csv")
    # new_data = df.dropna()  #输出结果不会修改源数据
    df.dropna(subset=['ST_NUM'], inplace=True)  #移除ST_NUM为空的行
    print(df.to_string())


"""
    替换空值：fillna()
"""
def replace_data():
    df = pd.read_csv("property-data.csv")
    df["ST_NUM"].fillna('199', inplace=True)
    print(df.to_string())


"""
    列的均值（所有值加起来的平均值）:mean()
    中位数值（排序后排在中间的数）:median()
    众数（出现频率最高的数）:mode() 
"""
def count_data():
    df = pd.read_csv("property-data.csv")
    # var = df["ST_NUM"].mean()   #求列均值
    # var = df["ST_NUM"].median()  #求列中位数
    var = df["ST_NUM"].mode()   #求列众数
    df["ST_NUM"].fillna(var, inplace=True)
    print(df.to_string())


# """
#     清除格式错误的数据：
# """
# def format_error_data():
#     # 第三个日期格式错误
#     data = [['2023/04/01', 50], ['2023/04/02', 40], ['20230401', 45]]
#     df = DataFrame(data, index=["day1", "day2", "day3"], columns=["Date", "Duration"])
#     df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
#     print(df['Date'])



# na_determine()    #调用空值数据判断方法
# delete_data()   #调用删除空值数据方法
# replace_data()  #调用替换空值数据的方法
count_data()    #调用计算数据方法
# format_error_data()    #调用清除错误格式数据的方法



"""
    axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
    how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
    thresh：设置需要多少非空值的数据才可以保留下来的。
    subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
    inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据
"""
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
