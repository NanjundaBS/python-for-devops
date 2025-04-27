import requests
#get response url using github api doc
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complet_detail = response.json()

for i in range(len(complet_detail)):
   print(complet_detail[i]['user']["login"])
