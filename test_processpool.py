from concurrent.futures import ProcessPoolExecutor

import requests

from timer import timer

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 5)
def main():
    with ProcessPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 100, [URL] * 100)
            executor.shutdown(wait=True)