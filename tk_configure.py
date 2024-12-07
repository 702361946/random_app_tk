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

    
logging.info('tk_configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
