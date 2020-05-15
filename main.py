import os
import requests
import argparse
import json
from dotenv import load_dotenv

def shorten_link(token, url):
    response = requests.get('https://' + url)
    response.raise_for_status()
    url_bitlinks = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url_bitlinks, headers={'Authorization': ("Bearer " + token)},
                             json={'long_url': ('https://' + url)}).json()
    return response['id']


def count_clicks(token, url):
    response = requests.get('https://' + url)
    response.raise_for_status()
    url_total_clicks = ('https://api-ssl.bitly.com/v4/bitlinks/{}/clicks').format(url)
    response = requests.get(url_total_clicks, headers={'Authorization': ("Bearer " + token)}).json()
    return response


if __name__ == '__main__':
    load_dotenv()
    
    token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser(description='Сокращение ссылки или подсчет кликов!')
    parser.add_argument('url', help='ссылка')
    args = parser.parse_args()
    url = args.url

    if url.startswith('bit.ly'):
        try:
            print(count_clicks(TOKEN, 'bit.ly/3bnVNi8'))
        except requests.exceptions.ConnectionError:
            print('Некорректная ссылка!')
    else:
        try:
            bitlink = shorten_link(TOKEN, url)
            print('Битлинк', bitlink)
        except requests.exceptions.ConnectionError:
            print('Некорректная ссылка!')
