# -*- coding: utf-8 -*-
# @File:user.py
# @Author: Zhang Ze
# @Date:   2024-09-03
# @Last Modified by:   Zhang Ze
import pandas as pd
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from common.config import con

router = APIRouter()


@router.get("/api/user")
async def u_test():
    sql = 'select member_id,member_name,member_wechat,remarks from tb_member '
    df = pd.read_sql(sql, con)
    out = df.to_dict()
    return JSONResponse(out)
