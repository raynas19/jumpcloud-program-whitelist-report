import json 
import requests


#Application WhiteList and Deny List
approved = ['Application 1', 'Application 2']
not_approved = []

## JUMPCLOUD API VALIDATION
url = "https://console.jumpcloud.com/api/v2/systeminsights/programs"
querystring = {"skip":"0",
               "limit":"1000",
               }

headers = {
    "x-org-id": "X-ENTER-ORG-ID",
    "x-api-key": "X-ENTER-API-KEY"
}

r = requests.request("GET", url, headers=headers, params=querystring)

# JSON Convertion
jc_data = r.json()
jc_dump = json.dumps(jc_data, indent=2)

# LOG Variables
i = 0
application_name = jc_data[i]['name']
program_publisher = jc_data[i]['publisher']
program_install_date = jc_data[i]['install_date']
program_install_source =jc_data[i]['install_source']
system_id = jc_data[i]['system_id']

# PROGRAM

file = open('Not_Approved_Programs.txt', 'w')

for audit in jc_data:
    if application_name not in approved: 
        file.write('Not an approved application:'+ ', ' + application_name + ', '+ 'Publisher ,' + program_publisher + ' ,' + 'System ID: ,' + system_id + ' , ' + 'Install Date: ,' + program_install_date + ' , ' + 'Install Source: ' + ',' + program_install_source + '\n')
        r = requests.request("GET", url, headers=headers, params=querystring)
        jc_data = r.json()
        jc_dump = json.dumps(jc_data, indent=2)
        i += 1
        application_name = jc_data[i]['name']
        #white_list.append()
        continue

    else:
         file.write('Approved Application:' + ', '+ application_name + ', '+ 'Publisher ,' + program_publisher + ' ,' + 'System ID: ,' + system_id + ' , ' + 'Install Date: ,' + program_install_date + ' , ' + 'Install Source: ' + ',' + program_install_source + '\n')
         r = requests.request("GET", url, headers=headers, params=querystring)
         jc_data = r.json()
         jc_dump = json.dumps(jc_data, indent=2)
         i += 1
         application_name = jc_data[i]['name']
         continue

