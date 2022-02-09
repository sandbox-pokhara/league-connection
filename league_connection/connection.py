from urllib.parse import urljoin

import urllib3
from requests import Session

from .info import get_connection_info

__all__ = [
    'LeagueConnection',
]


class LeagueConnection(Session):
    def __init__(self, lockfile, timeout=30):
        super().__init__()
        urllib3.disable_warnings()
        self.info = get_connection_info(lockfile, timeout=timeout)

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.info['url'], url)
        kwargs['auth'] = self.info['username'], self.info['password']
        kwargs['verify'] = False
        return super().request(method, url, *args, **kwargs)
