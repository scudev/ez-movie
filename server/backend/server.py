# -*- coding: utf-8 -*-

from fastapi import FastAPI

api = FastAPI()


@api.get('/')
async def root():
    return {"message": "Hello World"}

@api.get('video/detail')
async def videoDetail(pwd: str):
    return {'message': 'hello world'}

@api.get('video/list')
async def videoList(pwd: str):
    return {'message': 'hello world'}

@api.post('video/status')
async def videoStatus():
    pass