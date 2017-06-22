__author__ = "s4g4"
__date__ = "$6 June, 2016 4:00:00 PM$"

#!/usr/bin/python

import sys
sys.path.append("..")
from config import config
import hashlib
import requests,json
import threading
import datetime
from time import sleep

def getPass(line):
    string_arr = line.split(":")
    return string_arr[0].strip()

def genAllHashes(password):
    data={}
    data['password']=password
    data['md5'] = hashlib.md5(password).hexdigest()
    data['sha1'] = hashlib.sha1(password).hexdigest()
    data['sha256'] = hashlib.sha256(password).hexdigest()
    data['date']= datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    return data

def store(data):
    es_url = config.get('ES_URL')
    search_string ='{ "query":{ "query_string" : { "default_field" : "password","analyzer" : "whitespace", "query" : "\\"'+data['password']+'\\"" } }}'
    result = requests.post(es_url+"/_search", data=search_string)
    data1 = result.json()
    if not bool(data1['hits']['hits']):
        query_string_json = json.JSONEncoder().encode(data)
        result = requests.post(es_url, data=query_string_json)
    

def main_loop():
    with open('input.txt') as fp:
        counter = 0
        line_no = 0
        for line in fp:
            line_no = line_no+1 
            try:
                print line
                password = getPass(line)
                data = genAllHashes(password)
                store(data)
                counter = counter+1

            except Exception as e:
                print ("problem with line", line,". exception is ", e)

            #appending in the done file    
            with open("done.txt", "w") as myfile:
                myfile.write(str(line_no))

#            sys.exit()
            sleep(0.01)        
    print "Data Imported Finished, total = %s" % counter
            
            
if __name__ == "__main__":
    
    main_loop()
    