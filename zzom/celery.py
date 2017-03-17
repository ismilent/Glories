#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery
from celery import platforms

from config import CELERY_CONF

celery_app = Celery()
platforms.C_FORCE_ROOT = True
celery_app.config_from_object(CELERY_CONF)

if __name__ == '__main__':
    celery_app.start()