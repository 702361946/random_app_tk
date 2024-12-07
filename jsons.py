#  Copyright (c)
import json
import logging
from datetime import datetime

from _path import root_logger, file_path

if True:
    root_logger.name = 'jsons'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def w_json(a, name: str, encoding: str = 'utf-8'):
    logging.info(f'w_json\\name:{name}\n{a}')
    try:
        with open(f'{file_path}{name}.json', 'w+', encoding=encoding) as f:
            json.dump(a, f, indent=4, ensure_ascii=False)
            return True

    except Exception as e:
        logging.error(e)
        # print(e)
        return False


def r_json(name: str, encoding: str = 'utf-8'):
    logging.info(f'r_json\\name:{name}')
    try:
        with open(f'{file_path}{name}.json', 'r+', encoding=encoding) as f:
            a = json.load(f)
            return a

    except Exception as e:
        logging.error(e)
        # print(e)
        return None

logging.info('json ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
