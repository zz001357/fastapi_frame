# -*- coding: utf-8 -*-
# @File:main.py
# @Author: Zhang Ze
# @Date:   2024-09-03
# @Last Modified by:   Zhang Ze
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api
from common.config import load_toml, config_dir

app = FastAPI()
# 跨域
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

# 方法一
# app.include_router(project.router)
# app.include_router(about.router)

# 方法二
app.include_router(router=api)


@app.get("/")
async def test():
    return {"message": "Hello World"}


if __name__ == '__main__':
    run = load_toml(config_dir)['run']
    uvicorn.run(app='main:app', host=run['host'], port=run['port'], reload=False)
