#!/usr/local/bin/python3

import base64
import configparser
import urllib.parse
import urllib.request

config = configparser.ConfigParser()
config.read('config.ini')

with open('script.groovy', 'r', encoding='UTF-8') as file:
    groovy_script = file.read()
url = f"{config['general']['host']}/scriptText"
parameters = {'script':groovy_script}
data = urllib.parse.urlencode(parameters).encode('utf-8')
req = urllib.request.Request(url=url, data=data)

username = config['cred']['username']
password = config['cred']['password']
cred = base64.b64encode(f'{username}:{password}'.encode('utf-8'))
req.add_header("Authorization", f"Basic {cred.decode('utf-8')}")

s = urllib.request.urlopen(req)
result = s.read().decode('utf-8')
print(result)
