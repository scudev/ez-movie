# -*- coding: utf-8 -*-

from fastapi import FastAPI
from src import redis
api = FastAPI()


@api.get('/')
async def root():
    return {"message": "Hello World"}

@api.get('video/detail')
async def videoDetail(pwd: str):
    return {'message': 'hello world'}

@api.get('video/list')
async def videoList(pwd: str):
    vlist = await redis.rds_fetch_all_list(pwd)
    return vlist

@api.post('video/status')
async def videoStatus():
    pass