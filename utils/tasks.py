#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
from celery import task, current_task
from celery import Celery
from config import celeryConfig

app_celery = Celery()
app_celery.config_from_object(celeryConfig)

@task(name="tasks.qadd")
def add(a,b):
    print dir(current_task)
    print dir(task)
    return a+b
