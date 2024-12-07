import random
import subprocess
import sys
from tkinter import messagebox

from jsons import *

if True:
    root_logger.name = 'main_configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

default_configure = {
    "mode": "randint",
    "weight": {},
    "random_list": [],
    # "random_list_None_list_error": True # 用来检查过完权重后的list,list为空([])就报错,不过这玩意命名貌似有点长?貌似没什么用
}
mode_s = ['randint', 'list']
user_configure = default_configure
temp = {}


def sys_exit(message: str = None):
    logging.info(f'sys exit:{message}')
    sys.exit()


def save_configure(_configure: dict = None):
    if _configure is None:
        _configure = user_configure
    logging.info('save configure')
    w_json(_configure, 'configure')


def up_save_configure() -> dict:
    def configure_file_error():
        logging.error('配置文件未知')
        messagebox.showerror('error', '读取配置文件时出错,请检查是否有手动修改错误')
        if messagebox.askquestion('info', '是否需要重置配置?'):
            logging.info('重置配置文件')
            _re = default_configure
            save_configure(re)
            return _re
        else:
            subprocess.Popen(['notepad.exe', f"{file_path}configure.json"], shell=True)
            sys_exit('配置错误,主动退出')

    logging.info('up save configure')
    re = r_json('configure')
    if re is None:
        re = configure_file_error()

    for _k in default_configure.keys():
        if _k not in re.keys():
            re = configure_file_error()

    # 权重翻新
    for k in re['weight'].keys():
        try:
            re['weight'][int(k)] = re['weight'].pop(k)
        except TypeError:
            pass
    logging.info(f'weight\n{re["weight"]}')

    return re


def r_configure():
    """
    重置configure
    """
    logging.info('r configure')
    save_configure(default_configure)
    messagebox.showinfo('info', '重置完成,重启应用生效')


def save_settings(mode):
    logging.info(f'save settings\nmode:{mode}')
    if mode in mode_s:
        user_configure['mode'] = mode
        save_configure(user_configure)
    else:
        messagebox.showinfo('error', '请检查模式是否存在')

    messagebox.showinfo('info', '保存完成,重启应用生效')


def random_randint(_a: int, _b: int):
    logging.info(f'randint\\a:{_a}\\b:{_b}')
    try:
        _a = int(_a)
        _b = int(_b)
    except Exception as e:
        logging.error(f'{e}')

    if type(_a).__name__ != 'int':
        logging.info('a not int')
        messagebox.showerror('randint error', message="最小值不为整数")
    elif type(_b).__name__ != 'int':
        logging.info('b not int')
        messagebox.showerror('randint error', message="最大值不为整数")
    elif _a >= _b:
        logging.info('a >= b!')
        messagebox.showerror('randint error', message="最小值不能大于等于最大值")
    else:
        _r = list(range(_a, _b + 1))
        # 权重
        for k in user_configure['weight'].keys():
            if type(k).__name__ == 'int':
                if _b >= k >= _a:
                    if user_configure['weight'][k] >= 1:
                        for i in range(user_configure['weight'][k] - 1):
                            _r.append(k)
                    elif user_configure['weight'][k] < 1:
                        # 删除掉权重小于1的
                        del _r[k]

        if not _r: # 删完权重可能一个不剩
            logging.error('抽取列表为空')
            messagebox.showerror('error', '请检查权重设置,确保抽取列表中有可以抽取出来的')
            return False

        logging.debug(f'randint_list\n{_r}')
        _r = _r[random.randint(_a, len(_r) - 1)]
        logging.info(f'randint:{_r}')
        messagebox.showinfo('randint', message=f"抽出来了:\n{_r}")
        return True


def random_list(_a: list):
    logging.info(f'list\\a:{_a}')
    if type(_a).__name__ != 'list':
        logging.error('_a type not list')
        messagebox.showerror('error', '不为列表!请检查logging以确认传入参')

    _r = _a
    for k in _r:
        if k in user_configure['weight'].keys():
            if user_configure['weight'][k] > 1:
                for i in range(user_configure['weight'][k] - 1):
                    _r.append(k)
            elif user_configure['weight'][k] < 1:
                # 删除掉权重小于1的
                del _r[k]

    if not _r: # 删完权重可能一个不剩
        logging.error('抽取列表为空')
        messagebox.showerror('error', '请检查权重设置,确保抽取列表中有可以抽取出来的')
        return False

    logging.debug(f'random_list\n{_r}')
    _r = _r[random.randint(0, len(_r) - 1)]
    logging.info(f'list:{_r}')
    messagebox.showinfo('list', message=f'抽出来了:\n{_r}')


def random_list_settings():
    logging.info('settings random list')
    subprocess.Popen(['notepad.exe', f"{file_path}configure.json"], shell=True)
    subprocess.Popen(['notepad.exe', ".\\README.md"], shell=True) # 这个没有也无关紧要
    messagebox.showinfo('info', '请修改键"random_list",修改完成后请保存并重启应用')
    messagebox.showinfo('info', '按下确定以退出')
    sys_exit('作者无能,无法写出列表编辑器,用户将自行修改,程序退出以保证其不会再用')


logging.info('main_configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

if __name__ == '__main__':
    logging.debug('main_configure DEBUG')
    # user_configure = up_save_configure()
    # save_configure()
    # print(up_save_configure())
    # random_list_settings()
    pass
