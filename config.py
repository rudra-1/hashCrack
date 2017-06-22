
__author__ = "s4g4"
__date__ = "$6 Jun, 2016 4:04:29 PM$"

'''
1. have to find how to search words '123!' in ES
2. replace that in code
3. clear db and collect from starting
'''
config = {

    "ES_URL" : "http://localhost:9200/hashdictionary/passwords"
}

'''
es_mapping  = 
    {
      "mappings": {
        "passwords": { 
          "properties": {
            "date":    { "type": "date"}, 
            "password":    { "type": "string","index": "not_analyzed"}, 
            "md5":    { "type": "string","index": "not_analyzed"}, 
            "sha1":    { "type": "string","index": "not_analyzed"}, 
            "sha256":    { "type": "string","index": "not_analyzed"} 
          }
        }
      }
    }
'''