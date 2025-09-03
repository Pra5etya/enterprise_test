import redis

class RedisClient:
    def __init__(self):
        self.client = None

    def init_app(self, app):
        self.client = redis.Redis(
            host = app.config["REDIS_HOST"],
            port = app.config["REDIS_PORT"],
            db = 0,
            decode_responses = True
        )
        app.redis = self.client

redis_client = RedisClient()
