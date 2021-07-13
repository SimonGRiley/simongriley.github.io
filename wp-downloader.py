import requests
import os
from pathlib import Path

domain = "https://ebryx.com/"
working_directory = "./assets"
url_list = open("urls.txt",'r')

currentdirectory = os.getcwd()
print("running from:" + currentdirectory)
lines = url_list.readlines()

if not os.path.exists(working_directory):
    os.mkdir(working_directory)

for line in lines:
    line = line.strip()
    url = line
    line = line.replace(domain,"")
    dir_struct = line.split("/")
    expected_path = working_directory
    count = 0
    for i in range(0,len(dir_struct)):
        directory_name = dir_struct[i]
        if directory_name == dir_struct[-1]:
            resource_file = requests.get(url)
            with open(expected_path + "/" + directory_name, 'w+') as new_file:
                new_file.write(str(resource_file.content))
        else:
            if not os.path.exists(expected_path+directory_name):
                os.chdir(expected_path)
                print("creating: " + directory_name + " in " + expected_path)
                try:
                    os.mkdir(directory_name)
                except:
                    pass
                expected_path = expected_path + "/" + directory_name
                os.chdir(currentdirectory)
    os.chdir(currentdirectory)

url_list.close()
