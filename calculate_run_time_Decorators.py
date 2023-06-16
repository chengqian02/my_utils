import functools
import time
import datetime
import logging

# 计算运行时间装饰器
def runTime(func):
    @functools.wraps(func)
    def run(*args, **kwargs):
        start_time = time.time()
        results = func(*args, **kwargs)
        # 记录程序结束时间
        end_time = time.time()
        # 计算程序运行时间并格式化输出
        run_time = datetime.timedelta(seconds=(end_time - start_time))
        formatted_run_time = str(run_time).split(".")[0]
        logging.info(f"程序运行时间为：{formatted_run_time}")
        return results
    return run

# 装饰器_展示经过的时间、传入的参数、调用的结果
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
    return clocked