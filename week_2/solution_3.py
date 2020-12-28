#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import csv

res = requests.get(
    "https://directory.ntschools.net/api/System/GetAllSchools").content
parsed_data = json.loads(res)

magic_url = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="

endpoint = []
for i in parsed_data:
    endpoint.append(i["itSchoolCode"])

ls = []
for i in range(50):
    single_data = []
    data_res = requests.get(magic_url+endpoint[i]).content
    info = json.loads(data_res)
    single_data.append(info['name'])
    single_data.append(info['physicalAddress']['displayAddress'])
    single_data.append(
        info['schoolManagement'][0]['firstName'] + info['schoolManagement'][0]['lastName'])
    single_data.append(info['schoolManagement'][0]['position'])
    single_data.append(info['schoolManagement'][0]['email'])
    single_data.append(info['telephoneNumber'])
    ls.append(single_data)

with open("school_data.csv", "w") as file:
    file_writer = csv.writer(file)
    headers = ["Name", "Address", "Principal/Admin Name",
               "Principal/Admin Position", "Principal/Admin E-mail", "Telephone"]
    file_writer.writerow(headers)
    for i in range(len(ls)):
        file_writer.writerow(ls[i])

