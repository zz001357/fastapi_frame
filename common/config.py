# -*- coding: utf-8 -*-
# @File:config.py
# @Author: Zhang Ze
# @Date:   2024-09-05
# @Last Modified by:   Zhang Ze
import tomllib
from sqlalchemy import create_engine
from common.utils import load_toml

config_dir = 'common/config.toml'  # 指定配置文件路径

mysql = load_toml(config_dir)['mysql']
con = create_engine(mysql['db'])
