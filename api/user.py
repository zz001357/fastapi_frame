# -*- coding: utf-8 -*-
# @File:user.py
# @Author: Zhang Ze
# @Date:   2024-09-03
# @Last Modified by:   Zhang Ze
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/user")
async def u_test():
    return {"message": "测试网站跑通2"}
