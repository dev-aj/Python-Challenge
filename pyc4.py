import urllib.request
import re

base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

nothing = '63579' #try from start nothing =12345

for i in range(400):
    urlData = str(urllib.request.urlopen(base+nothing).read())
    nothing = re.findall('\d+', urlData)[0]
    print('Nothing: '+nothing)
    print(urlData)
