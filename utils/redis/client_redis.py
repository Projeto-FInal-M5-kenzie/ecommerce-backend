import os
import redis

redis_client = None

def get_redis_client():
    global redis_client

    if not redis_client:
        redis_client = redis.Redis(
            host=os.getenv('REDIS_HOST'),
            port=os.getenv('REDIS_PORT'),
            db=os.getenv('REDIS_DB'),
            password=os.getenv('REDIS_PASSWORD')
        )
        redis_client.ra
    assert redis_client.ping()
    return redis_client