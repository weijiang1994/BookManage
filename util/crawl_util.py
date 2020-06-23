"""
@Time    : 2020/6/23 10:55
@Author  : weijiang
@Site    : 
@File    : crawl_util.py
@Software: PyCharm
"""
import requests
import re

url = 'https://news.cnblogs.com/NewsAjax/GetRecommendNews?itemCount=10'


def get_cnblogs_recommend_news():
    res = requests.get(url=url)
    if res.status_code == 200:
        return res.text
    else:
        return False


def parse_news(news):
    news_urls = re.findall("href=\"(.*?)\"", news, re.S)
    news_titles = re.findall("<a .*?>(.*?)</a>", news, re.S)
    return news_titles[:-1], news_urls[:-1]


if __name__ == '__main__':
    news = get_cnblogs_recommend_news()
    content = parse_news(news)
    print(content)

