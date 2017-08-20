# coding: utf-8

import urllib.robotparser
import requests
from bs4 import BeautifulSoup


def fetch(url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; dispoler; https://dispodia.github.io/dispoler)'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup.p.string


if __name__ == '__main__':
    target_url = 'https://dispodia.github.io/robots-disallow-sample/'
    robots_txt_url = 'https://dispodia.github.io/robots-disallow-sample/robots.txt'

    print(target_url)

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_txt_url)
    rp.read()

    if rp.can_fetch('dispoler', target_url):
        print(fetch(target_url))
    else:
        print('cannot fetch')

    # ----------

    target_url = 'https://dispodia.github.io/robots-allow-sample/'
    robots_txt_url = 'https://dispodia.github.io/robots-allow-sample/robots.txt'

    print(target_url)

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_txt_url)
    rp.read()

    if rp.can_fetch('dispoler', target_url):
        print(fetch(target_url))
    else:
        print('cannot fetch')
