# coding: utf-8

from functools import wraps


"""
module in python 本身就是singleton的，当python作为模块被引入的时候，会检查当前目录下是否由.pyc文件，
如果有，就直接使用现有的.pyc文件，如果没有，则会创建.pyc文件。然后从.pyc文件中取得所需的对象。
.pyc文件是python源文件经过编译后生成的文件，是一种跨平台的字节码(byte code)，能够提高加载速度。
"""

############################################


class Singleton(object):
    """
    用__new__()来控制类的创建过程
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    pass


a1 = MyClass()
a2 = MyClass()

assert id(a1) == id(a2)

############################################


def singleton(cls):
    """
    利用装饰器实现单例过程
    """
    instance = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class AnoMyClass():
    pass


b1 = AnoMyClass()
b2 = AnoMyClass()

assert id(b1) == id(b2)

############################################


class _Singleton(type):
    """
    通过元类实现单例
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class OtherMyClass():
    __metaclass__ = _Singleton


c1 = OtherMyClass()
c2 = OtherMyClass()

assert id(c1) == id(c2)
