import requests
from bs4 import BeautifulSoup
import pprint
def get_hn_content():
    url = 'https://news.ycombinator.com/news'
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    return bs

def parse_hn_content(links, ratings):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        vote = ratings[idx].select('.subtext > .subline > .score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))

            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

if __name__ == '__main__':
    hn_content = get_hn_content()
    links = hn_content.select('.titleline > a')
    subtext = hn_content.select('.subtext')
    parsed_content = parse_hn_content(links, subtext)
    parsed_content.sort(key=lambda x: x['votes'], reverse=True)
    pprint.pprint(parsed_content)
