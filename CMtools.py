import time



def timer(func):
    def wrapper(*args, **kwds):
        t0 = time.time()
        func(*args, **kwds)
        t1 = time.time()
        print('耗时%0.3f' % (t1 - t0))
    return wrapper

# 方法2import datetime


# def count_time(func):
#     def int_time(*args, **kwargs):
#         start_time = datetime.datetime.now()  # 程序开始时间
#         func(*args, **kwargs)
#         over_time = datetime.datetime.now()   # 程序结束时间
#         total_time = (over_time-start_time).total_seconds()
#         print('程序共计%s秒' % total_time)
#     return int_time


@timer
def main():
    print('>>>>开始计算函数运行时间')
    for i in range(1, 1000):
        for j in range(i):
            print (j)
    for i in range(1, 1000):
        for j in range(i):
            print (j)

if __name__ == '__main__':
    main()