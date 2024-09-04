# -*- coding: utf-8 -*-
# @File:works.py
# @Author: Zhang Ze
# @Date:   2024-09-04
# @Last Modified by:   Zhang Ze
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/works")
async def u_test():
    return {"message": "作品"}
