import re
import urllib.request
import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
#this is just smth that I researched online to add color to the final result


while True:
    url="https://www.dictionary.com/browse/"
    word=input("Enter your word: ")

    url=url+word

    data=urllib.request.urlopen(url).read()
    data1=data.decode("utf-8")

    m=re.search('<meta name="description" content=', data1)
    start=m.end()+1
    end=m.end()+200
    string=data1[start:end]

    m=re.search('See more.">', string)
    start=0
    end=m.start()
    final=string[0:end]
    color.write(final+"\n","STRING")
