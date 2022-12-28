import json

#opening file from s3 for jfrog versions
def currentimagelist(filename,imagename='alpine'):
    with open(filename) as json_file:
        data = json.load(json_file)
    
    ii = imagename+'-images'
    dictalpine = data[ii]
    length = len(dictalpine)
        
    versionlist = []

    for i in range(length):
        versionlist.append(data[ii][i]['version'])

    return versionlist


def comparejson(hubjson='config-alpine.json'):
    with open(hubjson) as json_file:
        data = json.load(json_file)

    #jfrog
    jfrogimageversion = []
    filename = 'config1.json'
    jfrogimageversion = currentimagelist(filename)

    print("Displaying jfrog version and hub versions:  ")
    print(jfrogimageversion)
    print(data)


    

    for i in range(len(data)):
        for j in range(len(jfrogimageversion)):
            hubdata = data['alpine'+str(i)]
            if (hubdata) == jfrogimageversion[j] :
                print("matching")
            else:
                updateimageversion(hubdata)
    
def updateimageversion(version):
    filename = 'config1.json'
    outputfile = 'output-config.json'
    with open(filename) as json_file:
        data = json.load(json_file)
    listofdata = data['alpine-images']
    my_data = {'name': 'alpine', 'version': version, 'date': '23/12/2022 22:16:19', 'verified': 'true'}
    listofdata.append(my_data)
    
    my_final_dict = {'alpine-images': listofdata }
    print(my_final_dict)
    with open(outputfile, 'w') as f:
        json.dump(my_final_dict, f)

comparejson()