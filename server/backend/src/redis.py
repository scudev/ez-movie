# -*- coding: utf-8 -*-

import hashlib
from typing import List, Dict
import redis
from .model import *

redis_inst = redis.Redis(
    host='ezm-redis',
    port=6379,
    decode_responses=True
)


def hashid(prefix: str, val: str) -> str:
    sha1 = hashlib.sha1()
    sha1.update(val.encode('utf-8'))
    return prefix + sha1.hexdigest()[:6]


async def rds_fetch_all_list(pwd: str) -> List[Dict]:
    vids = redis_inst.keys(hashid('^', pwd))
    return redis_inst.mget(vids)