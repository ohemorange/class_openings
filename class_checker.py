import smtplib
from bs4 import BeautifulSoup
import urllib2

fromaddr = 'functorkitten@gmail.com'
toaddrs = 'eportnoy@princeton.edu'

msg = None

url = "http://registrar.princeton.edu/course-offerings/course_details.xml?courseid=002075&term=1134"
url_opener = urllib2.urlopen(url)
page = url_opener.read()
soup = BeautifulSoup(page)

cols = soup.find("table").find_all("tr")[4].find_all("td")
enrolled = int(str(cols[5])[30:32])
limit = int(str(cols[5])[57:59])
if enrolled < limit:
    msg = "436 "

url = "http://registrar.princeton.edu/course-offerings/course_details.xml?courseid=012261&term=1134"
url_opener = urllib2.urlopen(url)
page = url_opener.read()
soup = BeautifulSoup(page)

cols = soup.find("table").find_all("tr")[1].find_all("td")
enrolled = int(str(cols[5])[30:32])
if enrolled != 26:
    if msg == None:
        msg = "TRA "
    else:
        msg += "TRA "

url = "http://registrar.princeton.edu/course-offerings/course_details.xml?courseid=010457&term=1134"
url_opener = urllib2.urlopen(url)
page = url_opener.read()
soup = BeautifulSoup(page)

cols = soup.find("table").find_all("tr")[1].find_all("td")
enrolled = int(str(cols[5])[30:33])
limit = int(str(cols[5])[58:61])
if enrolled < limit:
    if msg == None:
        msg = "SOC 204 "
    else:
        msg += "SOC 204 "

url = "http://registrar.princeton.edu/course-offerings/course_details.xml?courseid=010455&term=1134"
url_opener = urllib2.urlopen(url)
page = url_opener.read()
soup = BeautifulSoup(page)

cols = soup.find("table").find_all("tr")[4].find_all("td")
enrolled = int(str(cols[5])[30:32])
limit = int(str(cols[5])[57:59])
if enrolled < limit:
    if msg == None:
        msg = "COS 340 Friday "
    else:
        msg += "COS 340 Friday "

cols = soup.find("table").find_all("tr")[2].find_all("td")
enrolled = int(str(cols[5])[30:32])
limit = int(str(cols[5])[57:59])
if enrolled < limit:
    if msg == None:
        msg = "COS 340 Thursday morning "
    else:
        msg += "COS 340 Thursday morning "

if msg != None:
    username = 'functorkitten'
    password = 'ocamldavewalker'    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
