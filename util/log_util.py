import logging
import logging.config
from util.global_var import *


# 日志配置文件：多个logger，每个logger指定不同的handler
# handler：设定了日志输出行的格式
#          以及设定写日志到文件（是否回滚）？还是到屏幕
#          还定了打印日志的级别
logging.config.fileConfig(LOG_CONF_FILE_PATH)
logger = logging.getLogger("example01")


def debug(message):
    logging.debug(message)


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def error(message):
    logging.error(message)


if __name__ == "__main__":
    debug("hi")
    info("gloryroad")
    warning("hello")
    error("这是一个error日志")