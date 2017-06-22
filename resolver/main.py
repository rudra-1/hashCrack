__author__ = "s4g4"
__date__ = "$6 June, 2016 6:00:00 PM$"

#!/usr/bin/python

import sys
sys.path.append("..")
from config import config
import hashlib
import requests,json
from time import sleep

def getHash(line):
    string_arr = line.split(":")
    return string_arr[0].strip()


def find(hash):
    es_url = config.get('ES_URL')
    search_string ='{ "query":{ "query_string" : { "fields" : ["sha1", "sha256","md5"],"analyzer" : "whitespace", "query" : "\\"'+hash+'\\"" } }}'
    result = requests.post(es_url+"/_search", data=search_string)
    data = result.json()
    if bool(data['hits']['hits']):
        return data['hits']['hits'][0]['_source']['password']
    else:
        return "0"
    
def storeInNewFile(line,password):
    line = line.strip()
    with open("cracked", "a") as myfile:
        myfile.write(line+":"+password+"\r\n")

    
if __name__ == "__main__":
    with open('input.txt') as fp:
        counter = 0
        line_no = 0
        for line in fp:
            line_no = line_no+1 
            try:
                print line
                hash = getHash(line)
		password = find(hash)
		if password != '0':
                    storeInNewFile(line,password)
                    counter = counter+1
                    
            except Exception as e:
                print ("problem with line", line,". exception is ", e)
            
            #appending in the done file    
            with open("done.txt", "w") as myfile:
                myfile.write(str(line_no))    
            #sys.exit()    
            sleep(0.01)   
    print "Data Imported Finished, total = %s" % counter 
    
