#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
BROKER_URL="redis://localhost:6379"
#BROKER_URL="amqp://"

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": '127.0.0.1',
    "port": '27017',
    "database": 'nmap',
    "taskmeta_collection": "celery_taskmeta",
}

#CELERY_RESULT_BACKEND="db+sqlite:///results.db"
#CELERY_TASK_SERIALIZER='json'
#CELERY_ACCEPT_CONTENT=['json']
#CELERY_RESULT_SERIALIZER='json'
#CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_IMPORTS=("module.tasks", )
