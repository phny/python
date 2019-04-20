#coding:utf-8



'''
python函数装饰器demo
'''
# def use_logging(func):
#     def wrapper(*args, **kwargs):
#         print('in func warpper')
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
# @use_logging
# def foo(name):
#     print('hello {}'.format(name))
#
# foo('tom')


def use_logging2(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                print('{} is run in info level '.format(func.__name__))
                func(*args)
            elif level == 'warn':
                print('{} run in warn level'.format(func.__name__))
                func(*args, **kwargs)
        return wrapper
    return decorator

@use_logging2(level='warn')
def foo2(name):
    print('hello {}'.format(name))

foo2('tony')
