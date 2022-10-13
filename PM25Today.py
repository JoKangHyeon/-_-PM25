import requests
import xml.etree.ElementTree as et
import datetime

serviceKey = "SERVICE KEY HERE"
#data.go.kr
stationName = "%EC%A3%BC%EC%95%88"
response = requests.get("http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey={0}&returnType=xml&numOfRows=24&pageNo=1&stationName={1}&dataTerm=DAILY&ver=1.0".format(serticeKey,stationName))
ele = et.fromstring(response.content)

body = ele.find("body")
items = body.find("items")

for i in items:
  timetext=i.find("dataTime").text
  plusday = False
  
  if timetext.split()[1]=='24:00':
      plusday = True
      timetext = timetext.replace('24:00','00:00')
      
  time = datetime.datetime.strptime(timetext, '%Y-%m-%d %H:%M')
  if plusday:
      time = time.replace(day=time.day+1)
  today = datetime.date.today()

  if time.date()==today:
    print("{0} pm25 is : {1}".format(time,i.find("pm25Value").text))
  