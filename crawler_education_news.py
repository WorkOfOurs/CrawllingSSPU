# Code Creation Date: 2025-11-03
# Purpose: (Currently) crawl down info from department of education affairs from SSPU
import time
import requests
from bs4 import BeautifulSoup

# 目标地址是SSPU的教务处官网
base_url = "https://jwc.sspu.edu.cn"
target_url = base_url + "/895/list.htm"

# 简单定义头部，写个UA足矣
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.55 Safari/537.36"
}

if __name__ == "__main__":
    request_object = requests.get(target_url, headers=headers)
    soup = BeautifulSoup(request_object.content, "html.parser")
    news_items = (soup.find(class_="news_list")
                  .find_all("li", class_="news"))

    print("== SSPU教务处新闻资讯通知 ==")
    for news_item in news_items:
        time.sleep(0.25)
        print("条目:")
        print(news_item.get_text())
        print("地址:")
        print(base_url + news_item.find("a")["href"])
        print("---")
