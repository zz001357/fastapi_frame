# -*- coding: utf-8 -*-
# @File:user.py
# @Author: Zhang Ze
# @Date:   2024-09-03
# @Last Modified by:   Zhang Ze
import fastapi
import pandas as pd
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from common.config import con
from fastapi.requests import Request

router = APIRouter()


@router.get("/api/user")
async def u_test():
    sql = 'select member_id,member_name,member_wechat,remarks from tb_member '
    df = pd.read_sql(sql, con)
    out = df.to_dict()
    return JSONResponse(out)


# 使用Query  方式获取前端传递的参数
@router.get("/api/user2")
async def u_test2(request: Request):
    query_params = request.query_params
    print(type(query_params))
    member_id = query_params.get("id2")
    print(member_id)
    return {"Request": query_params}


# 使用json 方式获取前端传递的参数
@router.get("/api/user3")
async def u_test3(request: Request):
    # 因为是迭代一个异步函数。所以需要使用await
    json_data = await request.json()
    print(json_data)
    return {"Request": json_data}


# 使用json 方式post传递
@router.post("/api/user4")
async def u_test4(request: Request):
    # 因为是迭代一个异步函数。所以需要使用await
    json_data = await request.json()
    print(json_data)
    return {"ok"}


# 使用json 方式获取前端传递的参数,但是是同步方法就需要用到Pydantic模型定义一个json结构
class User5(BaseModel):
    id3: int
    name: str


@router.get("/api/user5")
def u_test5(user5: User5):
    print(user5)
    print(user5.id3)
    print(user5.name)
    return {"Request": user5}


@router.post("/api/user6")
def u_test6(user6: User5):
    print(user6)
    print(user6.id3)
    print(user6.name)
    return {"Request": user6}
