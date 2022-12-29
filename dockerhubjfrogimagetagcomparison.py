import requests
import ast 
import json
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Making a GET request to get the content from dockerhub repo and the status code
def dockerhubimageupdate():
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

    #my_info = {}
    #my_info['alpine-images'] = alpine_images
    #print(my_info)
    json_object = json.dumps(my_information, indent = 4) 
    print(json_object)
    filename = "config-" + imagename + ".json"
    with open(filename, 'w') as f:
        json.dump(my_information, f)

def currentimagelist(filename,imagename):
    #imagename = input("Enter the image name: ")
    with open(filename) as json_file:
        data = json.load(json_file)
    
    ii = imagename+'-images'
    dictalpine = data[ii]
    length = len(dictalpine)
        
    versionlist = []

    for i in range(length):
        versionlist.append(data[ii][i]['version'])

    return versionlist


def comparejson():
    hubdet = input("Enter the image name: ")
    hubjson = "config-" + hubdet + ".json"
    with open(hubjson) as json_file:
        data = json.load(json_file)

    #jfrog
    jfrogimageversion = []
    filename = 'config' + hubdet + '.json'
    jfrogimageversion = currentimagelist(filename,hubdet)

    print("Displaying jfrog version and hub versions:  ")
    print(jfrogimageversion)
    print(data)


    for i in range(len(data)):
        for j in range(len(jfrogimageversion)):
            hubdata = data[hubdet+str(i)]
            if (hubdata) == jfrogimageversion[j] :
                print("matching")
            else:
                updateimageversion(hubdata,filename,hubdet)
    
def updateimageversion(version,filename,imagename):
    #filename = 'config1.json'
    outputfile = 'output-config.json'
    with open(filename) as json_file:
        data = json.load(json_file)
    imgstr = imagename+'-images'
    listofdata = data[imgstr]
    my_data = {'name': imagename, 'version': version, 'date': dt_string, 'verified': 'true'}
    listofdata.append(my_data)
    
    my_final_dict = {imgstr: listofdata }
    print(my_final_dict)
    with open(outputfile, 'w') as f:
        json.dump(my_final_dict, f)

dockerhubimageupdate()
comparejson()
