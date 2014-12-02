# coding=utf-8
'''
Created on 2014-10-23

@author: zenglizhi
'''

# 关于回调功能的测试
# Functor是这种回调功能的关键对象
class Functor:
    """Simple functor class."""
    def __init__(self, fn, *args):
        self.fn = fn
        self.args = args
    def __call__(self, *args):
        self.fn(*(self.args + args))
# 想对该函数进行回调操作        
def test_callback1(arg1, arg2):
    print "test_callback1", arg1, arg2
# 先进行简单地测试
obj_call1 = Functor(test_callback1, 1111, 'qweqwe111111111')
obj_call1()
# 结果：
# test_callback1 1111 qweqwe111111111
# 看看过程中带入参数的方式
def test_callback2(arg1, arg2, call_arg):
    print "test_callback2", arg1, arg2, call_arg
obj_call2 = Functor(test_callback2, 2222, 'qweqwe22222222')
obj_call2(222)  # 过程中输入参数，并且使回调函数得到这个参数
# 结果：
# test_callback2 2222 qweqwe22222222 222
# 再来看看对象中的方法被用来回调
# 基本原理与上面两个例子相同，但可以引入对象本身的函数
# 并且也可引入其他对象进行回调，那么它的用法将会非常丰富
class Test:
    def __init__(self):
        pass
    
    def test_callback1(self, arg1, arg2):
        print "Test.test_callback 1111", arg1, arg2
    
    def test_callback2(self, arg1, arg2, call_arg):
        print "Test.test_callback 2222", arg1, arg2, call_arg
        
    def test_callback_arg(self):
        obj_call1 = Functor(self.test_callback1, 1111, 'qweqwe1111')
        print "obj_call1 = ", obj_call1
