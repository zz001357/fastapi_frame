# -*- coding: utf-8 -*-
# @File:router.py
# @Author: Zhang Ze
# @Date:   2024-09-04
# @Last Modified by:   Zhang Ze
from fastapi import APIRouter

from api import user, works

api = APIRouter()
api.include_router(user.router)
api.include_router(works.router)

__all__ = ['api']
