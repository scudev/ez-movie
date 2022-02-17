FROM python:3.9-alpine

COPY ./requirements.txt ./

RUN python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple