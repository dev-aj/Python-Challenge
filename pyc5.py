import pickle
#import urllib.request

infile = open(b"banner.p", 'rb')

data = pickle.load(infile)

infile.close()

#print(data)

for p in data:
    print("".join(i*j for i,j in p))
