# -*- coding: utf-8 -*-

import redis
from .model import *

redis_inst = redis.Redis(
    host='ezm-redis',
    port=6379,
    decode_responses=True
)