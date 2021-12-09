# import required modules
from bs4 import BeautifulSoup
import requests
import json
import re

s = "Suga_(rapper)"
data = {}

def scrape():

    # get URL
    page = requests.get("https://en.wikipedia.org/wiki/{str}".format(str=s))

    # scrape webpage
    soup = BeautifulSoup(page.content, 'html.parser')

    heads = soup.find_all('h2')

    for head in heads:
        if head.find('span', id = "Personal_life"):
            para = head.find_next_sibling('p')
            para = para.text
            text = re.sub(r'\[.*?\]+', '', para)
            text = text.replace('\n', '')
            print(text)
            
            data = {s: text}
            to_json(text,s)
            # to_json(data,s)



def to_json(data,title):

    with open('{str}.txt'.format(str=s), 'w') as f:

        lines = [s, data]
        f.write('\n'.join(lines))
        f.close()


# def to_json(data,title):

#     f = open('{title}.json'.format(title = title), 'w')
#     f.write(json.dumps(data))
#     f.close()


def startpy():
    scrape()


if __name__ == '__main__':
    startpy()