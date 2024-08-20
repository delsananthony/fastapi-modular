# -*- charset:utf-8 -*-
# abstract service class

from abc import ABC


class BaseServices(ABC):

    @classmethod
    def read(cls, *args, **kwargs):
        pass

    @classmethod
    def write(cls, *args, **kwargs):
        pass

    @classmethod
    def create(cls, *args, **kwargs):
        pass

    @classmethod
    def unlink(cls, *args, **kwargs):
        pass


AbstractServices = BaseServices


class SVC(AbstractServices):
    pass
