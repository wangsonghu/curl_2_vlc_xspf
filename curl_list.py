import re
import sys
import requests
from jinja2 import FileSystemLoader, Environment

url = sys.argv[1]
#url = 'https://web-server.hosts.songhu.wang/study/%5B1.%5D%5Bipv6%5D'

list= []

x = requests.get(url, verify=False)
raw_list = re.compile(r'<a href=".*">').finditer(x.text.strip())
for item in raw_list:
    item = str(item.group())
    if item != '<a href="../">':
        item = url + item[9:-2]
        list += [item]

j2_loader = FileSystemLoader('./')
env = Environment(loader=j2_loader)
j2_tmpl = env.get_template('./list.j2')
results = j2_tmpl.render(list = list)

with open('/out/list.xspf', mode='a+', encoding='utf-8') as f:
    f.truncate(0)
    f.write(results)
