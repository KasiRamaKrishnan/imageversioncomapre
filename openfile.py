import json


def currentimagelist(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    

    dictalpine = data['alpine-images']
    length = len(dictalpine)
        
    versionlist = []

    for i in range(length):
        versionlist.append(data['alpine-images'][i]['version'])

    return versionlist


ll = []
filename = 'config1.json'
ll = currentimagelist(filename)
print(ll)
 
