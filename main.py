import tkinter

from main_configure import *
from tk_configure import *

if True:
    root_logger.name = '_main'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main():
    win = tk.Tk()
    win.title('random app')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    win.protocol("WM_DELETE_WINDOW", lambda: sys_exit("user in main page exit"))

    logging.info(f'mode:{user_configure["mode"]}')
    if user_configure['mode'] == 'randint':
        _min = pack_entry(win, default_text='请输入最小值', y=0)
        _max = pack_entry(win, default_text='请输入最大值', y=20)
        pack_button(win, '清空', lambda: delete_entry_s([_min, _max]), x=0, y=70)
        pack_button(
            win,
            '抽取',
            lambda: random_randint(get_entry(_min), get_entry(_max)),
            x=80,
            y=70
        )

    elif user_configure['mode'] == 'list':
        pack_button(win, '编辑列表', lambda: random_list_settings(win), x=0, y=70)
        pack_button(win, '抽取', lambda: random_list(user_configure["random_list"]), x=80, y=70)

    else:
        messagebox.showerror('error', '未知模式,请检查设置')
        settings_page(win)

    pack_button(win, '设置', lambda: settings_page(win), x=165, y=70)

    win.mainloop()


def settings_page(win: tkinter.Tk):
    logging.info('settings page\n')
    # 隐藏主窗口避免多个settings窗口出现
    withdraw_win(win)

    sub_window = tk.Tk()
    sub_window.title("app settings")
    sub_window.geometry(win_geometry)
    sub_window.resizable(win_resizable[0], win_resizable[1])

    # 监听窗口关闭事件
    sub_window.protocol("WM_DELETE_WINDOW", lambda: sys_exit("user in settings page exit"))

    pack_button(
        sub_window,
        "返回",
        lambda: [close_win(sub_window), deiconify_win(win)],
        x=165,
        y=70
    )
    pack_button(
        sub_window,
        '权重编辑',
        lambda: weight_settings(sub_window),
        x=100,
        y=70
    )
    pack_button(
        sub_window,
        '重置',
        lambda: r_configure(),
        y=70
    )

    pack_message(sub_window, '模式:')
    _mode = pack_entry(sub_window, x=50)
    pack_button(
        sub_window,
        '保存',
        lambda: [
            save_settings(get_entry(_mode)),
            delete_entry_s([_mode]),
        ],
        x=50,
        y=70
    )

    sub_window.mainloop()

    deiconify_win(win)


def random_list_settings(win: tk.Tk):
    logging.info('random list settings')

    withdraw_win(win)

    sub_window = tk.Tk()
    sub_window.title("list settings")
    sub_window.geometry(win_geometry)
    sub_window.resizable(win_resizable[0], win_resizable[1])

    # 监听窗口关闭事件
    sub_window.protocol(
        "WM_DELETE_WINDOW",
        lambda: sys_exit("user in random list settings page exit")
    )

    _list = pack_list(
        sub_window,
        h=5,
        yscrollcommand=True,
        _t=user_configure['random_list'],
        x=70
    )
    pack_button(sub_window, '保存', lambda: save_settings(
        random_list=get_list(_list, 0, tk.END)
    ), x=90, y=70)
    pack_button(sub_window, '取消', lambda: [
        close_win(sub_window),
        deiconify_win(win)
    ], x=165, y=70)
    entry = pack_entry(sub_window, x=90)
    pack_button(sub_window, '添加', lambda: [
        add_list(_list, get_entry(entry), tk.END),
        delete_entry(entry)
    ], x=90, y=20)
    pack_button(
        sub_window,
        '删除选中',
        lambda: delete_list(_list, _list.curselection()),
        x=140,
        y=20
    )

    sub_window.mainloop()

    deiconify_win(win)


def weight_settings(win: tk.Tk):
    logging.info('weight settings')

    withdraw_win(win)

    sub_window = tk.Tk()
    sub_window.title("weight settings")
    sub_window.geometry(win_geometry)
    sub_window.resizable(win_resizable[0], win_resizable[1])

    # 监听窗口关闭事件
    sub_window.protocol(
        "WM_DELETE_WINDOW",
        lambda: sys_exit("user in weight settings page exit")
    )

    _list = pack_list(
        sub_window,
        h=5,
        yscrollcommand=True,
        _t=user_configure['weight'].keys(),
        x=70
    )
    pack_button(sub_window, '保存', lambda: save_settings(
        weight=get_list(_list, 0, tk.END) # <-乐
    ), x=90, y=70)
    pack_button(sub_window, '取消', lambda: [
        close_win(sub_window),
        deiconify_win(win)
    ], x=165, y=70)
    entry = pack_entry(sub_window, x=90)
    pack_button(sub_window, '添加', lambda: [
        add_list(_list, get_entry(entry), tk.END),
        delete_entry(entry)
    ], x=90, y=20)
    pack_button(
        sub_window,
        '删除选中',
        lambda: delete_list(_list, _list.curselection()),
        x=140,
        y=20
    )

    sub_window.mainloop()

    deiconify_win(win)


if __name__ == "__main__":
    main()
