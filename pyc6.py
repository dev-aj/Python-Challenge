import zipfile
import re

comments = []
filename = '90052.txt'

with zipfile.ZipFile('channel.zip') as file:
    count = len(file.infolist()) - 1
    for f in range(count):
        comments.append(file.getinfo(filename).comment.decode("utf-8"))
        data = file.read(filename).decode("utf-8")
        if(re.search('\d+',data)):
            nothing = re.findall('\d+', data)[0]
        else:
            print('Else: ', data)
        filename = ''+nothing+'.txt'
print("".join(comments))
