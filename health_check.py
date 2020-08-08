import json
from http import HTTPStatus
from typing import List

import requests

from slack import send_error_case, send_shutdown_case


def main():
    target_urls = get_target_urls_from_file()
    for url in target_urls:
        try:
            r = requests.get(url=url)
            if r.status_code >= HTTPStatus.NOT_FOUND:
                send_error_case(target_url=url, http_status=r.status_code)
        except Exception:
            send_shutdown_case(url)


def get_target_urls_from_file(file_path='./target.json') -> List:
    with open(file_path, 'r') as f:
        return json.loads(f.read()).get('target_url', [])


main()
