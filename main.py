import tkinter

from main_configure import *
from tk_configure import *

if True:
    root_logger.name = '_main'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 值配置
user_configure = up_save_configure()


def main():
    win = tk.Tk()
    win.title('random app')
    win.geometry(win_geometry)
    win.resizable(win_resizable[0], win_resizable[1])

    logging.info(f'mode:{user_configure["mode"]}')
    if user_configure['mode'] == 'randint':
        _min = pack_entry(win, default_text='请输入最小值', y=0)
        _max = pack_entry(win, default_text='请输入最大值', y=20)
        pack_button(win, '清空', lambda: delete_entry_s([_min, _max]), x=0, y=70)
        pack_button(
            win,
            '抽取',
            lambda: [random_randint(get_entry(_min), get_entry(_max)), delete_entry_s([_min, _max])],
            x=80,
            y=70
        )

    elif user_configure['mode'] == 'list':
        pack_button(win, '编辑列表', lambda: random_list_settings(), x=0, y=70)
        pack_button(win, '抽取', lambda: random_list(user_configure["random_list"]), x=80, y=70)

    else:
        messagebox.showerror('error', '未知模式,请检查设置')
        settings_page(win)

    pack_button(win, '设置', lambda: settings_page(win), x=165, y=70)

    win.mainloop()


def settings_page(win: tkinter.Tk):
    # 隐藏主窗口避免多个settings窗口出现
    withdraw_win(win)

    sub_window = tk.Tk()
    sub_window.title("app settings")
    sub_window.geometry(win_geometry)
    sub_window.resizable(win_resizable[0], win_resizable[1])

    # 监听窗口关闭事件
    sub_window.protocol("WM_DELETE_WINDOW", lambda: sys_exit("user in settings page exit"))

    pack_button(sub_window, "返回", lambda: [close_win(sub_window), deiconify_win(win)], x=160, y=70)
    pack_button(
        sub_window,
        '重置',
        lambda: [r_configure(), messagebox.showinfo('info', '重置成功,重启应用生效')],
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
        x=80,
        y=70
    )

    sub_window.mainloop()

    deiconify_win(win)


if __name__ == "__main__":
    main()
