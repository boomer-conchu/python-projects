#boomer conchu
#HentaiSenpai

import urllib
import urllib.request #this needs to be imported so we can use the urlopen
from bs4 import BeautifulSoup

#note: in the below url the fieldx=0: x = to desired field cart to update
#to change the field that were manipulating, change the number after the word "field" in the URL below.
dataPut = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=G9X0K7EWYIKC0O2F&field6=0" +str(1100))
print(dataPut)
