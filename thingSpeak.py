#Boomer Conchu
#HentaiSenpai

#URL: https://api.thingspeak.com/channels/1651362/feeds.json?results=2 <- this is the Get Data Feed API
#We should consider just using the Field API, but this code is written in a way that will allow us to seek the data from the DataFeed API

import urllib
import urllib.request
import re #regular expression will help us search data in a string
from bs4 import BeautifulSoup


#get data from ThingsSpeak
#NOTE:WE MIGHT HAVE TO SWITCH FROM PRIVATE TO PUBLIC CHANNEL IN THIGNSPEAK FOR THIS TO WORK!!!!!
getData = urllib.request.urlopen("https://api.thingspeak.com/channels/1635476/feeds.json?results=2")
#print(getData) #-> wont show anything intelligilble
#print(getData.read()) #-> will get us all the data in the feed so this is why we needed to import re to allow us to search the data
#select = repr -> manipulates to repr which will allow us to make the data searchable
#select = re.search() -> allows us to search the data
select = repr(getData.read()) #this combines lines 18 & 19
select = select[300:] #shortens line 20. prints string from from after the 200 and stores it in this variable

#searching requires 2 parameters: (what we want to search in the expressions/string, which string we want the expression from )
show1 = re.search('field1":"(.+?)",',select) #"(.+?)"" -> gets us the content within the quotes  #FieldChart1 Nitrogen

#print the data
#Nitrogen
if show1:
	print(show1.group(1))
	if show1:
		exec(open("ts1.py").read()) #run pump code first
		if show1:
			exec(open("ts2.py").read()) #run servo code
#Phosphororus
show2 = re.search('field2":"(.+?)",',select)
if show2:
	print(show2.group(1))
	if show2:
		exec(open("ts1.py").read())
		if show2:
			exec(open("ts2.py").read())

#Potassium
show3  = re.search('field3":"(.+?)",',select)
if show3:
	print(show3.group(1))
	if show3:
		exec(open("ts1.py").read())
		if show3:
			exec(open("ts2.py").read())

#Soil Temp
show4  = re.search('field4":"(.+?)",',select)
if show4:
	print(show4.group(1))
	if show4:
		exec(open("ts1.py").read())
		if show4:
			exec(open("ts2.py").read())

#Soil Moisture
show5  = re.search('field5":"(.+?)",',select)
if show5:
	print(show5.group(1))
	if show5:
		exec(open("ts1.py").read())
		if show5:
			exec(open("ts2.py").read())

#test field <-this is used to test the field we can manipulate to see if things are moving.
show6 = re.search('field6":"(.+?)",',select)
if show6:
	print(show6.group(1))
	if show6:
		exec(open("ts1.py").read()) #run pump code first
		if show6:
			exec(open("ts2.py").read()) #run servo code


#start arguments to start pumps
#method 1: import servos.py then call the functions within this code since it has been imported
#if showX =< X:
	#servo.panTilt()

#method 2: using exec() funciton
#if showX =< X:
	#exec(open("servo.py).read())






