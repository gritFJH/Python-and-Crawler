#电子邮件的操作
import time
import os
import sys
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email
def guanji():      #此函数负责发送关机的标题（即guan）给邮箱
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('username@sina.com', 'password')
    to = ['username@sina.com']
    content = MIMEText('chong')
    content['Subject'] = 'chong'
    content['From'] = 'username@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('username@sina.com', to, content.as_string())
    sent.close() #关闭邮箱
def chongqi():     #此函数负责发送重启的标题（即chong）给邮箱
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('username@sina.com', 'password')
    to = ['username@sina.com']
    content = MIMEText('chong')
    content['Subject'] = 'chong'
    content['From'] = 'username@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('username@sina.com', to, content.as_string())
    sent.close()  # 关闭邮箱

def chongzhi():     #此函数负责发送刷新的标题（即reflash）给邮箱
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('username@sina.com', 'password')
    to = ['username@sina.com']
    content = MIMEText('')
    content['Subject'] = 'reflash'
    content['From'] = 'username@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('username@sina.com', to, content.as_string())
    sent.close()  # 关闭邮箱

def read():     # 读取邮件
    read = poplib.POP3('pop.sina.com')
    read.user('username@sina.com')  # 这里设置登录帐号
    read.pass_('password')
    tongji = read.stat()    # 返回邮件的基本统计信息
    str = read.top(tongji[0], 0)  # 服务器将返回由参数标识的邮件前0行内容，最后str为一个列表，有三个元素
    str2 = []
    for x in str[1]:  # 其中str[1],也就是str中的第二个参数为第一封邮件的各种信息，在这里要给其进行编码
        try:
            str2.append(x.decode())
        except:
            try:
                str2.append(x.decode('gbk'))
            except:
                str2.append(x.decode('big5'))
    msg = email.message_from_string('\n'.join(str2))  # 这个方法能把string的邮件转换成email.message实例
    # msg是把经过编码的str2转化为可识别的邮件信息，并且每行信息.join()来连接字符串
    biaoti = decode_header(msg['subject'])
    if biaoti[0][1]:  # 如果有第二个元素，就说明有编码信息
        biaoti2 = biaoti[0][0].decode(biaoti[0][1])
    else:
        biaoti2 = biaoti[0][0]
    #此时成功获取到最近一封邮件标题，即biaoti2
    if biaoti2 == "guan":
        return 0
    if biaoti2 == "chong":
        return 1
    read.quit()

if __name__ == '__main__': #当运行此程序时，读取邮件
    while True:
        time.sleep(2)
        if read() == 0:
            os.system('shutdown -s -t 1')
            chongzhi()
            break
        if read() == 1:
            os.system('shutdown -r')
            chongzhi()
            break


