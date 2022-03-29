import urllib
import urllib.request
import json
import requests


getdata = requests.get('https://api.thingspeak.com/channels/1635476/feeds.json?results=2').json() #use API Read and form into a json
print(getdata) #output of the json
channelID = getdata['channel']['id'] #isolate the channel and id info

field1 = getdata['feeds'] #iso the feeds field
#print(field1)
moist = [] #create blank list
for x in field1:
    #print(x['field1'])
    moist.append(x['field1'])
    #print(moist)
newMoist = int(moist[0]) #convert into an integer
print(f"moisture reading is: {newMoist}") #used f manipulation to put int into str
if newMoist <= 1000: #compares newMoist to set theshhold
    print("Plant needs water.")  #if less than the threshold: initiate the next code
    #exec(open("master/servo code.py").read()))#<-----insert new code here
else:
    print("Plant does not need water.") #if at or greater than threshold, code does not need to run
    #exec(open("master/servo code.py").read()))#<-----insert new code here
