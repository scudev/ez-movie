# -*- coding: utf-8 -*-
from enum import Enum, auto
from datetime import datetime
from pydantic import BaseModel


class VideoTag(Enum):
    OnlineFree = 0
    OnlineAuth = 1
    Offline = 2
    def __int__(self):
        return self.value


class OPStatus(Enum):
    Init = 0
    Working = 1
    Succeed = 2
    Timeout = 3
    Refused = 4
    Failed = 5
    def __int__(self):
        return self.value


class VideoInfo(BaseModel):
    vid: str = '#'
    tag: int
    info: str
    name: str
    brief: str
    created_time: str = None
    auth_info: str = None


class OPRecord(BaseModel):
    rid: str = '^'
    password: str
    vid: str
    op_time: str = None
    status: int = OPStatus.Init
