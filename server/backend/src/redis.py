# -*- coding: utf-8 -*-

import hashlib
from datetime import datetime
from typing import List, Dict

import redis
import ujson

from .model import *

redis_inst = redis.Redis(
    host='ezm-redis',
    port=6379,
    decode_responses=True
)


def hashid(prefix: str, val: str) -> str:
    sha1 = hashlib.sha1()
    sha1.update(val.encode('utf-8'))
    return prefix + sha1.hexdigest()[:12]


async def rds_fetch_all_list(pwd: str) -> List[Dict]:
    rids = redis_inst.keys(hashid('^', pwd) + '*')
    oplist = map(lambda x: ujson.loads(x), redis_inst.mget(rids))
    reslist = []
    for op in oplist:
        reslist.append({**oplist, **await rds_get_video(op['vid'])})
    return reslist


async def rds_save_video(vinfo: VideoInfo) -> str:
    vinfo.created_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    vinfo.vid = hashid('#', vinfo.info)
    if not redis_inst.get(vinfo.vid):
        redis_inst.set(vinfo.vid, ujson.dumps(vinfo.dict()))
    return vinfo.vid


async def rds_save_record(pwd: str, vid: str, status: OPStatus) -> str:
    assert redis_inst.get(vid), 'vid not found'
    orc = OPRecord(
        rid=hashid('^', pwd) + hashid('-', vid),
        vid=vid,
        password=pwd,
        op_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        status=status
    )
    redis_inst.set(orc.rid, ujson.dumps(orc.dict()))
    return orc.rid


async def rds_get_video(vid: str) -> dict:
    vinfo = redis_inst.get(vid)
    assert vinfo, 'vid not found'
    vinfo_dict = ujson.loads(vinfo_dict)
    return vinfo_dict


async def rds_del_video(pwd: str, vid: str) -> int:
    '''
    返回删除后剩余vid计数
    '''
    rid = hashid('^', pwd) + hashid('-', vid)
    redis_inst.delete(rid)
    remain = len(redis_inst.keys('*' + hashid('-', vid)))
    if remain == 0:
        redis_inst.delete(vid)
    return remain
