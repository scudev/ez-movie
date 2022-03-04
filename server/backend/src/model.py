# -*- coding: utf-8 -*-
from enum import Enum, auto
from datetime import datetime
from pydantic import BaseModel


class VideoTag(Enum):
    OnlineFree = 0
    OnlineAuth = 1
    Offline = 2


class OPStatus(Enum):
    Init = auto()
    Working = auto()
    Succeed = auto()
    Timeout = auto()
    Refused = auto()
    Failed = auto()


class VideoInfo(BaseModel):
    vid: str = '#'
    tag: VideoTag
    info: str
    created_time: datetime = None
    auth_info: str = None


class OPRecord(BaseModel):
    rid: str = '^'
    password: str
    vid: str
    op_time: datetime = None
    status: OPStatus = OPStatus.Init
