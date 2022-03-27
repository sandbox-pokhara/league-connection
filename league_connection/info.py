import os
import time

from .exceptions import ConnectionTimeoutError


def get_connection_info(lockfile, timeout=30):
    start = time.time()
    while True:
        if time.time() - start > timeout:
            raise ConnectionTimeoutError('Please make sure the client is running.')
        if not os.path.exists(lockfile):
            time.sleep(1)
            continue
        with open(lockfile, 'r') as fp:
            data = fp.read()
            data = data.split(':')

            if len(data) < 5:
                time.sleep(1)
                continue

            return {
                'url': f'{data[4]}://127.0.0.1:{data[2]}',
                'port': int(data[2]),
                'username': 'riot',
                'password': data[3],
                'method': data[4],
            }
