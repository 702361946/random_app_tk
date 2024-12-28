#  Copyright (c)
import logging
# UI部分
import tkinter as tk
from datetime import datetime

from _path import root_logger

# 窗口配置
win_geometry = '200x100'
win_resizable = (False, False)

# 抄作业
# 主窗口
"""
win = tk.Tk()
win.title('')
win.geometry(win_geometry)
win.resizable(win_resizable[0], win_resizable[1])
"""

# 子窗口
"""
sub_window = Toplevel(win)
sub_window.title("")
sub_window.geometry(win_geometry)
sub_window.resizable(win_resizable[0], win_resizable[1])
"""

# 日志初定义
if True:
    # 修改root logger的名称
    root_logger.name = 'tk_configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def close_win(win: tk.Tk):
    """
    关闭窗口
    """
    logging.info(f'window destroy')
    win.destroy()


def withdraw_win(win: tk.Tk):
    """
    隐藏窗口
    """
    logging.info('withdraw win')
    win.withdraw()


def deiconify_win(win: tk.Tk):
    """
    显示窗口
    """
    logging.info('deiconify win')
    win.deiconify()


# 布置文本
def pack_message(win: tk.Tk, t_text: str, t_width: int=100, x: int = 0, y: int = 0):
    """
    布置文本
    """
    logging.info(f'pack message:{t_text}')
    tk.Message(win, text=t_text, width=t_width).place(x=x, y=y)


# 布置按钮
def pack_button(win: tk.Tk, t_text: str, t_command, x: int = 0, y: int = 0):
    """
    布置按钮
    """
    logging.info(f'pack button:{t_text}')
    tk.Button(win, text=t_text, command=t_command).place(x=x, y=y)


# 布置输入框
def pack_entry(win: tk.Tk, t_width: int=100, default_text: str=None, x: int = 0, y: int = 0) -> tk.Entry:
    # default_text为默认文本
    logging.info(f'pack entry\\default_text:{default_text}')
    entry = tk.Entry(win, width=t_width)
    entry.place(x=x, y=y)

    if default_text:
        # noinspection PyUnusedLocal
        def set_default_text(event=None):
            """当输入框失去焦点且为空时，设置默认文本"""
            if not entry.get():
                entry.insert(0, default_text)

        # noinspection PyUnusedLocal
        def clear_default_text(event=None):
            """当输入框获得焦点且有默认文本时，清除文本"""
            if entry.get() == default_text:
                entry.delete(0, tk.END)

        # 默认文本
        entry.insert(0, default_text)

        # 绑定焦点事件
        entry.bind("<FocusIn>", clear_default_text)
        entry.bind("<FocusOut>", set_default_text)

    return entry


# 获取输入框
def get_entry(entry: tk.Entry) -> str:
    t_str = entry.get()
    logging.info(f'get entry:{t_str}')
    return t_str


# 清空输入框
def delete_entry(entry: tk.Entry):
    logging.info('entry delete')
    entry.delete(0, tk.END)


def delete_entry_s(s: list):
    logging.info('entry delete\\s')
    for i in s:
        delete_entry(i)


def pack_list(
        win: tk.Tk,
        h: int = 1,
        w: int = 10,
        yscrollcommand: bool = False,
        x: int = 0,
        y: int = 0,
        _t = None,
        lr: str = 'L'
    ) -> tk.Listbox:
    """
    用以创建一个列表
    :param win: 父部件
    :param h: 行数
    :param w: 宽度
    :param yscrollcommand: 竖向滚动
    :param x: 滚动条组件左上角x位置
    :param y: 滚动条组件左上角y位置,是的没看错,就是滚动条
    :param _t: 插入的内容,必须为list,不然……
    :param lr: 控制组件贴边,只有两个状态,L,R
    :return: tk.Listbox组件
    """
    logging.info('pack list')

    if _t is None:
        _t = [None]
    else:
        _t = list(_t)

    _list = tk.Listbox(win, height=h, width=w)

    for i in _t:
        _list.insert(tk.END, i)

    if yscrollcommand:
        scrollbar = tk.Scrollbar(win, orient="vertical", command=_list.yview)
        _list.config(yscrollcommand=scrollbar.set)
        scrollbar.place(x=x, y=y, height=win_geometry.split('x')[1]) # 竖向滚动条

    match lr:
        case 'L':
            logging.info('pack L')
            _list.pack(side=tk.LEFT)
        case 'R':
            logging.info('pack R')
            _list.pack(side=tk.RIDGE)
        case _:
            logging.info('lr not L or R')
            _list.pack()

    return _list


def get_list(_list: tk.Listbox, a: int, b: int = None) -> list:
    logging.info(f'get list\\a:{a}\\b:{b}')
    if b is None:
        b = a
    return list(_list.get(a, b))


def add_list(_list: tk.Listbox, a: list, b: int = None):
    """
    向列表加个变量
    :param _list:
    :param a:
    :param b:
    :return:
    """
    logging.info(f'add list\\a:{a}\\b:{b}')

    if type(a).__name__ != 'list':
        a = [a]
    if b is None:
        b = tk.END

    for i in a:
        _list.insert(b, i)


def delete_list(_list: tk.Listbox, a: int, b: int = None):
    """
    删除指定范围内的值
    :param _list:
    :param a:
    :param b:
    :return:
    """
    logging.info(f'delete list\\a:{a}')

    _list.delete(a, b)

    
logging.info('tk_configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
