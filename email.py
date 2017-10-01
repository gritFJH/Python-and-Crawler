#电子邮件的操作
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

#如何登录邮箱
#按目的分为是为发送邮件而登录还是为了读取邮件而登录
#先说为发送邮件而登录的操作。一般来说，登录使用SMTP，发送使用POP
sent = smtplib.SMTP('smtp.sina.com')
sent.login('username@sina.com', 'password')#这里一定注意，填的是独立密码

#发送邮件
#刚才我们已经登陆了，现在需要设置发送内容然后发送即可
to = ['username@sina.com']
content = MIMEText('How are you ?')
content['Subject'] = 'hello'
content['From'] = 'username@sina.com'
content['To'] = ','.join(to)
sent.sendmail('username@sina.com', to, content.as_string())
sent.close() #关闭邮箱


#读取邮件
read = poplib.POP3('pop.sina.com')
read.user('username@sina.com')#这里设置登录帐号
read.pass_('password')
tongji = read.stat()
str = read.top(tongji[0], 0)#服务器将返回由参数标识的邮件前0行内容，最后str为一个列表，有三个元素
str2 = []
for x in str[1]:#其中str[1],也就是str中的第二个参数为第一封邮件的各种信息，在这里要给其进行编码
    try:
        str2.append(x.decode())
    except:
        try:
            str2.append(x.decode('gbk'))
        except:
            str2.append(x.decode('big5'))
msg = email.message_from_string('\n'.join(str2))#这个方法能把string的邮件转换成email.message实例
#msg是把经过编码的str2转化为可识别的邮件信息，并且每行信息.join()来连接字符串
biaoti = decode_header(msg['subject'])
if biaoti[0][1]:#如果有第二个元素，就说明有编码信息
    biaoti2 = biaoti[0][0].decode(biaoti[0][1])
else:
    biaoti2 = biaoti[0][0]
