#  Copyright (c)

import logging
import os
from datetime import datetime

# 获取当前用户的AppData路径
appdata_path = os.path.expanduser('~\\AppData')

# 检查操作系统，Windows，拼接LocalLow路径
if os.name == 'nt':
    log_path = os.path.join(appdata_path, 'LocalLow\\702361946\\random_app\\app.log')
    file_path = os.path.join(appdata_path, 'LocalLow\\702361946\\random_app\\')
else:
    # 对于其他系统，可能没有LocalLow，自定义路径
    log_path = '.\\app.log'  # 请根据实际情况修改
    file_path = '.\\'

# 目录补全
os.makedirs(os.path.dirname(file_path), exist_ok=True) # 虽然我并不知道.\\为什么需要补全)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

if True:
    logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'path'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info(f'log_path:{log_path}')

logging.info('path ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
