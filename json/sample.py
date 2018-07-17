#pip install <Module Name>
#Command : python3 sample.py

import urllib.request
import os
import json

# create a simple JSON array
jsonString = '{"100":9,"103":7}'

# change the JSON string into a JSON object
jsonObject = json.loads(jsonString)

# print the keys and values
for key in jsonObject:
    if not os.path.exists(key):
        os.makedirs(key)
    value = jsonObject[key]
    for i in range(value):
        link = "http://data.infokombinat.com/hairstyle2/" + key + "/" + str(i) + ".jpg"
        urllib.request.urlretrieve(link, key+"/"+link.split('/')[-1])
