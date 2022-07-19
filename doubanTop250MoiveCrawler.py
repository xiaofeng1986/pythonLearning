import requests
import re
from fake_useragent import UserAgent

def get_page(url):
    try:
        response = requests.get(url, headers={'User-Agent':UserAgent().random})
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions:
        return None

def get_parse(html):
    parse = re.compile('li.*?"title">(.*?)</span>',re.S)
    parse_over = re.findall(parse,html)
    for item in parse_over:
        yield item

def save(items):
    for item in items:
        with open('title.csv','a') as f:
            f.write(item + '\n')


if __name__ == '__main__':
    for num in range(0,250,25):
        url = "https://movie.douban.com/top250"+ "?start="+str(num)+"&filter"
        html = get_page(url)
        items = get_parse(html)
        save(items)
        for item in items:
            print(item)
