# -*- coding: utf-8 -*-

from fastapi import FastAPI
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
    return {"message": "Hello World"}

@api.get('/v/detail')
async def videoDetail(pwd: str):
    return {'message': 'hello world'}

@api.get('/v/list')
async def videoList(pwd: str):
    vlist = await redis.rds_fetch_all_list(pwd)
    return vlist

@api.post('/v/add')
async def videoAdd(pwd: str, vinfo: model.VideoInfo):
    print(pwd, vinfo)
    return {}
