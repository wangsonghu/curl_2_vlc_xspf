import re
import sys
import requests
from jinja2 import FileSystemLoader, Environment

url = sys.argv[1]
#url = 'https://web-server.hosts.songhu.wang/study/%5B1.%5D%5Bipv6%5D'

list = []
# 定义视频文件的后缀
video_suffixs = ['mp4', 'flv', 'avi', 'rmvb', 'mkv', 'mkv', 'mov', 'wmv']
# 判断是否是视频文件标志位. 0：非视频 >0：是视频
flag = 0

# 请求URL
x = requests.get(url, verify=False)
# 删选文件列表
raw_list = re.compile(r'<a href=".*">').finditer(x.text.strip())
# 遍历文件列表
for item in raw_list:
    item = str(item.group())
    # 排除 <a href="../">
    if item != '<a href="../">':
        # 筛选视频文件
        for video_suffix in video_suffixs:
            video_suffix = '.'  + video_suffix + '">'
            # 如果是视频文件，flag的值+1
            if item.endswith(video_suffix):
                flag += 1
        # 如果是视频文件，将文件追加到列表
        if flag > 0:
            item = url + item[9:-2]
            list += [item]
# 准备渲染 j2模板位置
j2_loader = FileSystemLoader('./')
env = Environment(loader=j2_loader)
# j2 模板文件
j2_tmpl = env.get_template('./list.j2')
# 渲染
results = j2_tmpl.render(list = list)
# 打印结果
print(results)

# 写入文件
with open('/out/list.xspf', mode='a+', encoding='utf-8') as f:
    # 写入之前先清空文件
    f.truncate(0)
    f.write(results)
