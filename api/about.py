# -*- coding: utf-8 -*-
# @File:about.py
# @Author: Zhang Ze
# @Date:   2024-09-04
# @Last Modified by:   Zhang Ze
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/about")
async def u_test():
    return {"message": "关于"}
