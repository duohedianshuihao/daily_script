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
"""
__new__: 完成对象的创建，是类方法，返回值是实例化出来的实例
__init__: 完成对象的初始化，是实例方法，就是给__new__返回的实例赋初值
__call__: 对象可以使用call方法模拟函数的执行，obj.__call__(self, *args, **kwargs) 等同于 obj(*args, **kwargs)

下面OtherMyClass的执行过程可以看成，利用元类创建类，利用类实例化
元类创建类 --> OtherMyClass = _Singleton()  这里相当于调用了_Singleton.__new__() 和 _Singleton.__init__()
类的实例化 --> c1 = OtherMyClass()  由于OtherMyClass是_Singleton的实例，所以这里调用了_Singleton.__call__()

所以可以在这里利用元类实现单例
而且_Singleton.__call__()的调用在OtherMyClass.__new__()之前
"""


class _Singleton(type):
    """
    通过元类实现单例
    """
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = super(_Singleton, self).__call__(*args, **kwargs)
        return self._instance[self]


class OtherMyClass():
    __metaclass__ = _Singleton


c1 = OtherMyClass()
c2 = OtherMyClass()

assert id(c1) == id(c2)
