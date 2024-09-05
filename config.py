# -*- coding: utf-8 -*-
# @File:config.py
# @Author: Zhang Ze
# @Date:   2024-09-05
# @Last Modified by:   Zhang Ze
import tomllib


def load_toml(config_dir):
    with open(config_dir, 'rb') as f:
        config = tomllib.load(f)
    return config

