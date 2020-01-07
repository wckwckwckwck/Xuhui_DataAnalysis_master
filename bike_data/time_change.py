import time


def time_change_f(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
    # print(dt)


if __name__ == "__main__":
    dt1 = 1557695440
    print(time_change_f(dt1))
