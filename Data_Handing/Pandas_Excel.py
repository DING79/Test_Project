import pandas as pd


def write_data(path):
    data = pd.DataFrame({
        "id":[101,102,103,104,105,],
        "name":["A","N/A","C","D","na"],
        "age":[1,2,"N/A",4,5]
    })
    write = pd.ExcelWriter(path)    #输出路径
    data.to_excel(write)
    print("写入成功")


write_data(r"C:\Users\cyberway\Desktop\pandas_write.xlsx")  #输出位置

