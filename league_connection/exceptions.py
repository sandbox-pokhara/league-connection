class LeagueConnectionError(Exception):
    pass


class ConnectionTimeoutError(LeagueConnectionError):
    pass
