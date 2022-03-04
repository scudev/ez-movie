# -*- coding: utf-8 -*-

from fastapi import FastAPI
# for test
from fastapi.middleware.cors import CORSMiddleware

from src import redis
api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET', 'POST']
)

@api.get('/')
async def root():
    return {"message": "Hello World"}

@api.get('/video/detail')
async def videoDetail(pwd: str):
    return {'message': 'hello world'}

@api.get('/video/list')
async def videoList(pwd: str):
    vlist = await redis.rds_fetch_all_list(pwd)
    return vlist

@api.post('/video/status')
async def videoStatus():
    pass
