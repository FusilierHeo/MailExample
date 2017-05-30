# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.live.com', 587)
smtp.ehlo()  # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('sjhur1991@naver.com', 'skhur3319')

msg = MIMEText('본문 테스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = 'sjhur1991@naver.com'
smtp.sendmail('sjhur1991@naver.com', 'sjhur1991@naver.com', msg.as_string())

smtp.quit()

