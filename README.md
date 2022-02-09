# league-connection

league-connection is a python package to communicate to riot client and league client.

## Installation

```
pip install league-connection
```

## Examples

### Logging in (Riot Client)

```
>>> import os
>>> from league_connection import LeagueConnection
>>> lockfile = os.path.expanduser('~\\AppData\\Local\\Riot Games\\Riot Client\\Config\\lockfile')
>>> connection = LeagueConnection(lockfile, timeout=10)
>>> data = {'username': 'yourusername', 'password': 'yourpassword', 'persistLogin': False}
>>> res = connection.put('/rso-auth/v1/session/credentials', json=data)
>>> res.status_code
201
```

### Change summoner icon (League Client)

```
>>> from league_connection import LeagueConnection
>>> lockfile = 'C:\\Riot Games\\League of Legends\\lockfile'
>>> connection = LeagueConnection(lockfile, timeout=10)
>>> data = {'profileIconId': 1}
>>> res = connection.put('/lol-summoner/v1/current-summoner/icon', json=data)
>>> res.status_code
201
```
