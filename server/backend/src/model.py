# -*- coding: utf-8 -*-
from enum import Enum, auto
from datetime import datetime
from pydantic import BaseModel


class VideoTag(Enum):
    OnlineFree = auto()
    OnlineAuth = auto()
    Offline = auto()


class OPStatus(Enum):
    Init = auto()
    Working = auto()
    Succeed = auto()
    Timeout = auto()
    Refused = auto()
    Failed = auto()


class VideoInfo(BaseModel):
    uid: str
    tag: VideoTag
    info: str
    created_time: datetime
    auth_info: str = None


class OPRecord(BaseModel):
    uid: str
    password: str
    video_uid: str
    op_time: datetime
    status: OPStatus = OPStatus.Init
