# -*- coding: utf-8 -*-

import ujson
import datetime
import hashlib
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

async def save_video_info(video_json: dict):
    video_json['vid'] = hashid('#', video_json['info'])
    video_json['created_time'] = datetime.datetime.now()
    video_str = ujson.dumps(video_json)
    redis_inst.set(video_json['vid'], video_str)

async def save_op_record(record_json: dict):
    record_json['rid'] = hashid('^', record_json['password'] + record_json['vid'])
    record_json['op_time'] = datetime.datetime.now()
    record_json['status'] = OPStatus.Init
    record_str = ujson.dumps(record_json)
    redis_inst.set(record_json['rid'], record_str)

async def get_video_info(vid: str) -> VideoInfo:
    return VideoInfo(redis_inst.get(vid))

async def change_record_status(record_id: str, status: OPStatus) -> bool:
    pass