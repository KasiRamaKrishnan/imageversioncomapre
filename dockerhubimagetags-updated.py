import requests
import ast 
import json
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Making a GET request
imagename = input("Enter the image name: ")
url = 'https://hub.docker.com/v2/repositories/library/' + imagename + '/tags'
r = requests.get(url)
statuscode = r.status_code

# check status code for response received
# success code - 200
my_dict = {"version":"","date":[]}

versionlist = []
# print content of request
if statuscode == 200:
  ii = r.content
  byte_str = ii
  alpinejson = byte_str.decode("UTF-8")
  result = json.loads(alpinejson)
  #print(result)
  print("The last 2 stable verions for the image:",imagename,"are as below..")
  for i in range(3):
    versionlist.append(result['results'][i+1]['name'])
else:
  print("Give the correct image name..")

name = []
for i in range(2):
  con = imagename+str(i)
  name.append(con)

my_information = dict(zip(name, versionlist))
#print(my_information)

alpine_images = []

alpine_images.append(my_information)

#print(alpine_images)

my_info = {}
my_info['alpine-images'] = alpine_images
print(my_info)
json_object = json.dumps(my_information, indent = 4) 
print(json_object)
filename = "config-" + imagename + ".json"
with open(filename, 'w') as f:
    json.dump(my_information, f)


