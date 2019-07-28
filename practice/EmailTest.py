import smtplib


server = smtplib.SMTP('smtp.qq.com')
# server = smtplib.SMTP('pop.qq.com')
server.sendmail('dongshuicen@foxmail.com', '919427202@qq.com', 'python email test at 2019-07-29')
server.quit()
