# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
# for test
from fastapi.middleware.cors import CORSMiddleware

from src import redis
from src import model

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET', 'POST']
)


@api.get('/')
async def root():
    raise HTTPException(status_code=404, detail="route error")


@api.get('/v/detail')
async def videoDetail(vid: str):
    try:
        vinfo = await redis.rds_get_video(vid)
        return vinfo
    except:
        raise HTTPException(status_code=404, detail="vid not found")


@api.get('/v/list')
async def videoList(pwd: str):
    vlist = await redis.rds_fetch_all_list(pwd)
    return vlist


@api.post('/op/add_new')
async def opAddNew(pwd: str, vinfo: model.VideoInfo):
    vid = await redis.rds_save_video(vinfo)
    rid = await redis.rds_save_record(pwd, vid, model.OPStatus.Init)
    return {'vid': vid, 'rid': rid}


@api.post('/op/add_exist')
async def opAddExist(pwd: str, vid: str):
    try:
        rid = await redis.rds_save_record(pwd, vid, model.OPStatus.Init)
        return {'rid': rid}
    except:
        raise HTTPException(status_code=404, detail="vid not found")


@api.post('/op/delete')
async def opDelete(pwd: str, vid: str):
    remain = await redis.rds_del_video(pwd, vid)
    return {'remain': remain}
