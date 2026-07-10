import requests
import re

url = "https://raw.githubusercontent.com/ZhiXuanWang/cf-speed-dns/refs/heads/main/ipTop10.html"
resp = requests.get(url)
text = resp.text  # 获取页面内容

# 使用正则表达式匹配IPv4地址
ips = re.findall(r'\d+\.\d+\.\d+\.\d+', text)

# 将提取到的IP逐行写入 data/ip10.txt 文件
with open("data/ips.txt", "w") as f:
    for ip in ips:
        f.write(ip + "\n")
