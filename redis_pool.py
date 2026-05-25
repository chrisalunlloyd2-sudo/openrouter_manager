import redis
from redis import ConnectionPool

class RedisPool:
    def __init__(self, host, port, db, password):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.pool = ConnectionPool(host=host, port=port, db=db, password=password)

    def get_connection(self):
        return redis.Redis(connection_pool=self.pool)

    def close_connection(self, connection):
        connection.close()
