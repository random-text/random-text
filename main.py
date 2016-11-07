import random

import re

list = []
map = dict()
map2 = dict()

with open("words.txt", "r") as f:
    prev2Word = ""
    prevWord = ""
    for line1 in f:
        #print(line)
        line = re.sub('[A-Z|0-9|a-z|\<|\>|\-|\=|\:|\#|\d|\&|\;|\$|\%|\/]', "", line1)
        line = line.lower()
        for word in line.split(" "):

            string = word.replace("\n", "").replace(",", "").replace(".", "").replace("-", "").\
                lower().replace("?", "").replace("-","").replace("!", "").replace("(","").replace(")","").replace("\"","").lower()
            if prevWord != "" and string != "":
                if map.get(prevWord) == None:
                    map.update({prevWord: []})
                map.get(prevWord).append(string)

            if prev2Word != "" and string != "":
                if map2.get(prev2Word) == None:
                    map2.update({prev2Word: []})
                map2.get(prev2Word).append(string)

            prev2Word = prevWord + string
            prevWord = string

            if len(string) > 3:
                list.append(string)


#for i in range(0, 2000):
#    result = random.choice(list) + " " + random.choice(list) + " " + random.choice(list) + " " + random.choice(list) + " " + random.choice(list)



    #print(result)



def getText():
    curMap = list
    #random.seed(56)
    prevWord = ""

    result = ""
    for i in range(0, 40):
        for j in range(0, 10):

            if random.uniform(0, 1) < 0.0001 :
                word = random.choice(list)
            else :
                word = random.choice(curMap)
            #print(word)
            result += word.lower()
            result += " "
            curMap = map2.get(prevWord + word.lower())

            prevWord = word
            #print(curMap)


            if curMap == None or random.uniform(0, 1) < 0.2 :
                curMap = map.get(word)

            if curMap == None:
                curMap = list

        result += '<br>\n'


    return result

print "READED"
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(getText())


serv = HTTPServer(("localhost",8080), HttpProcessor)
serv.serve_forever()


