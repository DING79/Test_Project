from openpyxl import load_workbook
from colorama import Fore, Back, Style


def read_excel(path):
    # 文件路径
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "文件路径：" + Fore.LIGHTGREEN_EX + path)
    # 创建对象 读取文件
    lw = load_workbook(path, data_only=True)
    # 获取所有sheet
    sheets = lw.worksheets
    print(Fore.LIGHTMAGENTA_EX + "工作簿所有sheet：" + Fore.LIGHTGREEN_EX + str(sheets))
    # 输入想要获取的sheet名称
    sheet_name = input(Fore.LIGHTCYAN_EX + "请根据上面工作簿,输入sheet名称,查看对应信息：")
    for sheet_name_value in sheets:
        var = str(sheet_name_value)
        s_value = var.split('"')
        if sheet_name == s_value[1]:
            print(Fore.LIGHTMAGENTA_EX + "您当前想要查找的sheet名称为：" + Fore.LIGHTGREEN_EX + sheet_name)
            sheet = lw[sheet_name]
            # 读取所有列
            columns = sheet.columns
            print(Fore.LIGHTGREEN_EX + sheet_name + Fore.LIGHTMAGENTA_EX + "工作表内容如下：")
            # 迭代列读取
            for col in columns:
                col_value = []
                for row in col:
                    col_value.append(row.value)
                dic = {col_value[0]: col_value[1:]}
                print(Fore.LIGHTYELLOW_EX + str(dic))


# 传参：文件路径
read_excel(r"C:\Users\cyberway\Desktop\111.xlsx")
