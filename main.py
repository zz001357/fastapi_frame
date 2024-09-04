# -*- coding: utf-8 -*-
# @File:main.py
# @Author: Zhang Ze
# @Date:   2024-09-03
# @Last Modified by:   Zhang Ze
import uvicorn
from fastapi import FastAPI

from api import project, about
from api.router import api

app = FastAPI()
# 方法一
# app.include_router(project.router)
# app.include_router(about.router)

# 方法二
app.include_router(router=api)


@app.get("/")
async def test():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=9000, reload=True)
    # uvicorn.run(api='main:api', host='127.0.0.1', port=8000, reload=False)
