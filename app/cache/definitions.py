from functools import partial, update_wrapper
from fastapi_redis_cache import cache, FastApiRedisCache

redis_cache = FastApiRedisCache()

REDIS_CACHE_PREFIX = "fastapi-cache"

cache_half_a_second = partial(cache, expire=30)
update_wrapper(cache_half_a_second, cache)