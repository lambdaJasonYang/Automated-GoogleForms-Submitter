#jy1486 github
import http.client
import urllib.parse
import urllib.request
import random
import string
import re



#Let targetsite be https://docs.google.com/forms/d/e/EEEEEEEEEEEEEGGGGGGGGGGGGGGGGGGG/
#change urlin to your target site
urlin = 'https://docs.google.com/forms/d/e/EEEEEEEEEEEEEGGGGGGGGGGGGGGGGGGG/'

#set mmsg to your content
mmsg = 'Edit this part'




urlt = "".join(re.findall('https:\/\/docs.google.com(\/forms\/d\/e\/[0-9a-zA-Z-]*\/)',urlin))

url = urlt + 'viewform'
    
urlr = urlt + 'formResponse'

# the number of times you submit the form, note at numbers like 9999 you will have to wait a long time
numOfsubmit = 30


for i in range(0,(numOfsubmit + 1)):
    h2 = http.client.HTTPSConnection('docs.google.com:443')
    h4 = h2.connect()
    h2.request("GET",url) 
    h5 = h2.getresponse()
    src = h5.read().decode("utf-8)")
    stringg = re.findall('name="fbzx" value="(..[0-9]*)', src)
    stringy = "".join(stringg)
    
    urlh =  urlt + 'viewform?fbzx='+ stringy
    data = urllib.parse.urlencode({
	#look at source code of  google form to get name of entry
        #should look like '<input type="text" name="entry.5926704" '
        #if radio,dropdown,etc are used content must be limited to those options
#Edit the entry.__________ : ______ ,
         'entry.1547587782': mmsg,
         'entry.1643359058': mmsg,

         
         'fvv':'1',
         'draftResponse':'[,,"'+ stringy +'"]',
         'pageHistory':'0',
         'fbzx':stringy
         
         })

    
    header = {'referer' : urlh,
              'origin' :"https://docs.google.com",
              "content-type":"application/x-www-form-urlencoded",
              'Upgrade-Insecure-Requests': '1',
              'accept':'text/html'
              }
    
    h2.request("POST",urlr,data,header)
    h2.getresponse()
#print(h2.getresponse().read())
print(stringy)

