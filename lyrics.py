from bs4 import BeautifulSoup as bs
import sys
import re
import requests
singer=""
song=""
if len(sys.argv)==4: 
	singer=sys.argv[1].replace(' ','_')+"_%26_"+sys.argv[2].replace(' ','_')
	song=sys.argv[3]
elif len(sys.argv)==3:
	singer=sys.argv[1].replace(' ','_')
	song=sys.argv[2]
else:
	print("Usage: lyrics.py <artist(s)> <song>")
	exit()

doc = requests.get("http://lyrics.wikia.com/wiki/{0}:{1}".format(singer,song))
if doc.status_code == 200:
	soup = bs(doc.content,'html.parser')
	lyricsdoc = soup.find_all("div", class_="lyricbox")
	if len(lyricsdoc)<1:
	    print("Singer or song does not exist!")
	else:
	    s=str(lyricsdoc[0]).replace('<br/>','\n')
	    soup = bs(s,'html.parser')
	    print(soup.get_text())

else:
	print("connection error")
