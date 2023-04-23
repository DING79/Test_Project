#输出当前版本所有【关键字】
"""import keyword
var = keyword.kwlist
print(var)"""

#首行缩进,不需要用{}
"""if 条件:
    print('True')
else:
    print('False')"""

#数字类型(Number)
"""var = 99.8888
#整数类型
print('整数类型：')
print(int(var))
#布尔类型
print('布尔类型：')
print(bool(var))
#浮点类型
print('浮点类型：')
print(float(var))
#复数类型
print('复数类型：')
print(complex(var))"""

#字符串类型(String)
"""str = 'cyberway'
print('输出第一个字符：' + str[0])
print('输出倒数第一个字符：' + str[-1])
print('输出第2到第5个字符：' + str[1:4])
print('输出第3个之后的所有字符：' + str[2:])
print('输出从第1个到第8个每隔2步的字符：' + str[0:7:2])
print('输出空行：' + '\n')
print('输出不转义的字符：' + r'\n')"""

#不换行输出结果
"""var1 = 'cyber'
var2 = 'way'
print(var1)
print(var2)
print('-------------------')
print('输出不换行结果：')
print(var1,end='')
print(var2,end='')"""

#数据类型（自动转换）由小往大转，避免丢失数据
"""var_int = 123
var_flo = 1.23
var_new = var_int + var_flo
print('类型：',type(var_int))
print('类型：',type(var_flo))
print('结果：',var_new)
print('结果的类型是：',type(var_new))"""

#数据类型强制转换
"""var_int = 123
var_str = "456"
print('data:',var_int,end="")
print('; type:',type(var_int))
print('data:',var_str,end="")
print('; type:',type(var_str))
print('强制将str类型转换成int类型的结果为：',var_int + int(var_str))"""


#算数运算符
"""va1 = 2
var2 = 6
print('指数：',va1)
print('幂数：',var2)
var = va1**var2
print('指数幂结果为：',var)"""



#位运算符(以值的二进制数进行比较)
"""a = 118  #0111 0110
b = 69   #0100 0101
c = 0
#与 两者都是1 结果才为1
c = a & b
print('与运算c的值为：',c)  #0100 0100
#或 两者有一个是1 结果为1
c = a | b
print('或运算c的值为：',c)  #0111 0111
#异或 两者对位的值为异时 结果为1
c = a ^ b
print('异或运算c的值为：',c)  #0011 0011"""


#条件控制
"""age = abs(int(input('请输入你的年龄：')))
print('你的年龄是：',age)
if age < 18:
    print('你还未成年哦')
elif 18 <= age < 28:
    print('你好年轻哦')
elif 28 <= age < 50:
    print('你现在应该是一位成功人士哦')
else:
    print('年岁已高')
input('按enter退出')"""


#if嵌套
"""var = int(input('请输入一个数：'))
if var%2 == 0:
    if var%3 == 0:
        print('你输入的数能被2和3整除')
    else:
        print('你输入的数能被2整除，但不能被3整除')
else:
    if var%3 == 0:
        print('你输入的数能被3整除，但不能被2整除')
    else:
        print('你输入的数不能被2和3整除')"""


#match...case条件判断匹配
"""mycode = 200
print(http_code(200))
def http_code(code):
    match code:
        case 200:
            return 'OK'
        case 300:
            return 'waiting'
        case 400:
            return 'bad request'
        case 404:
            return 'not found'
        case _:
            return 'something...'"""



#while循环
"""num = int(input('请输入一个0-100的数，做求和计算：'))
sum = 0
count = 1
while count <= num:
    sum = sum + count
    count += 1
print(' 0 到',num,'求和的结果为：',sum)"""


#for循环
"""for var in range(1,10):
    if var == 5:
        print('数据为',var,'跳过继续执行')
        continue
    if var == 8:
        print('数据为',var,'退出循环')
        break
    print(var)
else:
    print('没有找到对应数据')
print('循环结束')"""


"""for num1 in range(1,10):
    for num2 in range(1,num1+1):
        if num1%num2 == 0:
            print(num1,'=',num2,'*',num1//num2)
            break
    else:
        print(num1,'是质数')"""


#输出结果的字体带颜色
from colorama import Fore,Back,Style

print(Fore.RED + "RED")
print(Fore.GREEN + "GREEN")
print(Fore.BLUE + "BLUE")
print(Fore.YELLOW + "YELLOW")
print(Fore.MAGENTA + "MAGENTA")
print(Fore.BLACK + "BLACK")
print(Fore.CYAN + "CYAN")
print(Fore.RESET + "RESET")
print(Fore.WHITE + "WHITE")
print("=========================")
print(Fore.LIGHTGREEN_EX + "LIGHTGREEN_EX")
print(Fore.LIGHTRED_EX + "LIGHTRED_EX")
print(Fore.LIGHTBLUE_EX + "LIGHTBLUE_EX")
print(Fore.LIGHTCYAN_EX + "LIGHTCYAN_EX")
print(Fore.LIGHTBLACK_EX + "LIGHTBLACK_EX")
print(Fore.LIGHTMAGENTA_EX + "LIGHTMAGENTA_EX")
print(Fore.LIGHTWHITE_EX + "LIGHTWHITE_EX")
print(Fore.LIGHTYELLOW_EX + "LIGHTYELLOW_EX")

print(Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + "Bg")
print(Back.RESET + Style.BRIGHT + "s")




























