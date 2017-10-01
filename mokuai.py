#远程控制开关机项目
#软件工程项目中，一般对于这种项目需要按照模块的思路去做，一个模块负责一项或者多项特定的功能，各个模块之间通过接口进行设计，在此模块指的是此模块中的函数
#模块划分

def guanji():
    a = 1
    #此函数负责发送关机的标题（guan）给邮箱
def chongqi():
    a = 1
    #此函数负责发送重启的标题（chong）给邮箱
def read():
    a = 1
    #此函数负责读取邮件中的指令，指令为guan返回0，指令为chong返回1
if _name_ == '_main_':
    if read() == 0:
        os.system('shutdown -s -t 1')
    if read() == 1:
        os.system('shutdown -r')