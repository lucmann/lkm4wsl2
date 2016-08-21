#!/usr/bin/env python
# - coding:utf-8 -
#
# Sun Aug 21 14:05:52 CST 2016

import urllib2
import random
import json
import sys
import smtplib
from email.mime.text import MIMEText 

reload(sys)
sys.setdefaultencoding('utf-8')

def get_jokes():
	appkey = ""
	url    = "http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1"
	req = urllib2.Request(url)
	req.add_header("apikey", appkey)
	response = urllib2.urlopen(req)
	content = response.read()
	if(content):
		random.seed()
		jsonvalues = json.loads(content)
		jokes_list = jsonvalues['showapi_res_body']['contentlist']
		joke_index = random.randint(0, len(jokes_list)-1)
		return u'(:每日一笑:)' + jokes_list[joke_index]['text']

def mailto(mailto_list, subject, content):
	mail_host = "smtp.qq.com"
	mail_user = "814640709@qq.com"
	mail_pswd = ""
	msg = MIMEText(content,
				   _subtype='plain',
				   _charset='utf-8')
	msg['Subject'] = subject
	msg['From']    = mail_user
	msg['To']      = ';'.join(mailto_list)

	try:
		smtp = smtplib.SMTP_SSL()
		smtp.connect(mail_host)
		smtp.login(mail_user, mail_pswd)
		smtp.sendmail(mail_user, mailto_list, msg.as_string())
		smtp.close()
		return True
	except Exception, e:
		print str(e)
		return False

if __name__ == '__main__':
	mailto_list = ['@139.com']
	if mailto(mailto_list, 
			  "S.M.I.L.E",
			  get_jokes()):
		print("Send mail succeed")
	else:
		print("Send mail fail")
