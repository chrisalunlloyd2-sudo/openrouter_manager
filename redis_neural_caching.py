import redis
import pickle
from typing import Any

class RedisNeuralCaching:
    def __init__(self, host: str, port: int, db: int):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = redis.Redis(host=host, port=port, db=db)

    def cache(self, key: str, value: Any):
        serialized_value = pickle.dumps(value)
        self.redis_client.set(key, serialized_value)

    def get(self, key: str) -> Any:
        serialized_value = self.redis_client.get(key)
        if serialized_value is None:
            return None
        return pickle.loads(serialized_value)

    def delete(self, key: str):
        self.redis_client.delete(key)
