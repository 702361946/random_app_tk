import logging
import random
from tkinter import messagebox

from jsons import *

if True:
    root_logger.name = 'main_configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

default_configure = {
    "settings_key": None,
    "mode": "randint",
    "weight": {}
}
mode_s = ['randint']
user_configure = default_configure
temp = {
    "settings_if": True
}

def save_configure(_configure: dict = None):
    if _configure is None:
        _configure = user_configure
    logging.info('save configure')
    w_json(_configure, 'configure')


def up_save_configure() -> dict:
    logging.info('up save configure')
    re = r_json('configure')
    if re is None:
        re = default_configure
        logging.error('未读取到配置\\创建默认配置')
        save_configure(re)

    return re


def r_configure():
    """
    重置configure
    """
    # 用for能避开pycharm的错误检查
    logging.info('r configure')
    save_configure(user_configure)


def save_settings(mode):
    logging.info(f'save settings\nmode:{mode}')
    if mode in mode_s:
        user_configure['mode'] = mode
    else:
        messagebox.showinfo('', '请检查模式是否存在')

    save_configure(user_configure)


def random_randint(a: int, b: int):
    logging.info(f'random\\a:{a}\\b:{b}')
    try:
        a = int(a)
        b = int(b)
    except Exception as e:
        logging.error(f'{e}')

    for k in user_configure['weight'].keys():
        try:
            user_configure['weight'][int(k)] = user_configure['weight'].pop(k)
        except TypeError:
            pass
    logging.info(f'weight\n{user_configure["weight"]}')

    if type(a).__name__ != 'int':
        logging.info('a not int')
        messagebox.showerror('randint error', message="最小值不为整数")
    elif type(b).__name__ != 'int':
        logging.info('b not int')
        messagebox.showerror('randint error', message="最大值不为整数")
    elif a >= b:
        logging.info('a >= b!')
        messagebox.showerror('randint error', message="最小值不能大于等于最大值")
    else:
        _r = list(range(a, b + 1))
        # 权重
        for k in user_configure['weight'].keys():
            if type(k).__name__ == 'int':
                if b >= k >= a:
                    if user_configure['weight'][k] >= 1:
                        for i in range(user_configure['weight'][k] - 1):
                            _r.append(k)
                    else:
                        # 删除掉权重为0的
                        del _r[k]
        logging.debug(f'randint_list\n{_r}')
        _r = _r[random.randint(a, len(_r) - 1)]
        logging.info(f'randint:{_r}')
        messagebox.showinfo('randint', message=f"抽出来了:\n{_r}")
        return True

if __name__ == '__main__':
    user_configure = up_save_configure()
    # save_configure()
    print(up_save_configure())
    pass
