import time


# 返回中文格式的日期：xxxx年xx月xx日
def get_chinese_date():
    year = time.localtime().tm_year
    if len(str(year)) == 1:
        year = "0" + str(year)
    month = time.localtime().tm_mon
    if len(str(month)) == 1:
        month = "0" + str(month)
    day = time.localtime().tm_mday
    if len(str(day)) == 1:
        day = "0" + str(day)
    return "{}年{}月{}日".format(year, month, day)


# 返回英文格式的日期：xxxx/xx/xx
def get_english_date():
    year = time.localtime().tm_year
    if len(str(year)) == 1:
        year = "0" + str(year)
    month = time.localtime().tm_mon
    if len(str(month)) == 1:
        month = "0" + str(month)
    day = time.localtime().tm_mday
    if len(str(day)) == 1:
        day = "0" + str(day)
    return "{}/{}/{}".format(year, month, day)


# 返回中文格式的时间：xx时xx分xx秒
def get_chinese_time():
    hour = time.localtime().tm_hour
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    minute = time.localtime().tm_min
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    second = time.localtime().tm_sec
    if len(str(second)) == 1:
        second = "0" + str(second)
    return "{}时{}分{}秒".format(hour, minute, second)


# 返回英文格式的时间：xx:xx:xx
def get_english_time():
    hour = time.localtime().tm_hour
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    minute = time.localtime().tm_min
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    second = time.localtime().tm_sec
    if len(str(second)) == 1:
        second = "0" + str(second)
    return "{}:{}:{}".format(hour, minute, second)


# 返回中文格式的日期时间
def get_chinese_datetime():
    return get_chinese_date() + " " + get_chinese_time()


# 返回英文格式的日期时间
def get_english_datetime():
    return get_english_date() + " " + get_english_time()


# 返回时间戳
def get_timestamp():
    year = time.localtime().tm_year
    if len(str(year)) == 1:
        year = "0" + str(year)
    month = time.localtime().tm_mon
    if len(str(month)) == 1:
        month = "0" + str(month)
    day = time.localtime().tm_mday
    if len(str(day)) == 1:
        day = "0" + str(day)
    hour = time.localtime().tm_hour
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    minute = time.localtime().tm_min
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    second = time.localtime().tm_sec
    if len(str(second)) == 1:
        second = "0" + str(second)
    return "{}{}{}_{}{}{}".format(year, month, day, hour, minute, second)


if __name__ == "__main__":
    print(get_chinese_datetime())
    print(get_english_datetime())