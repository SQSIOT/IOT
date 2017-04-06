import re
import smtplib
from smtplib import SMTP as SMTP
from bs4 import BeautifulSoup

SERVER = "smtp.gmail.com"
FROM = "iotcartest1@gmail.com"
TO = ['alexa123@gmail.com']

markup = open("C:\Users\SinghS01\Desktop\AI_Demo_erWin_automation\erWinTestReport.html")
soup = BeautifulSoup(markup.read())
#print soup.get_text()
searchObj = re.search( r'Status:(.*?) .*', soup.get_text(), re.M|re.I)
print searchObj.group(0)

msg = "\n" + searchObj.group(0)
s = smtplib.SMTP(SERVER, 587, timeout = 120)
s.ehlo()
s.starttls()
s.login("iotcartest1@gmail.com", "iot@123456")

s.sendmail(FROM, TO, msg)
s.quit()
markup.close()

