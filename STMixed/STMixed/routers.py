# -*- coding:utf8 -*-
from django.conf import settings

class ManagerRouter(object):

    def db_for_read(self, model, **hints):
        pass

    def db_for_write(self, model, **hints):
        pass

    def allow_relation(self, obj1, obj2, **hints):
        pass

    def allow_syncdb(self, db, model):
        pass