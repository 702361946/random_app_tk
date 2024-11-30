import tkinter

from tk_configure import *
from main_configure import *

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

    pack_button(win, '设置', lambda: settings(win), x=160, y=70)

    win.mainloop()


def settings(win: tkinter.Tk):
    def settings_key(_key: str, window):
        logging.info(f'settings_key:{_key}')
        if _key == user_configure['settings_key']:
            temp['settings_if'] = True
            close_win(window)

    # 隐藏主窗口避免多个settings窗口出现
    withdraw_win(win)

    # 用来指示是否可以启用设置
    temp['settings_if'] = True

    if user_configure['settings_key']:
        temp['settings_if'] = False
        messagebox.showinfo("info", "需要密码")

        sub_window = tk.Tk()
        sub_window.title("app settings")
        sub_window.geometry(win_geometry)
        sub_window.resizable(win_resizable[0], win_resizable[1])

        pack_button(sub_window, "返回", lambda: [close_win(sub_window), deiconify_win(win)], x=160, y=70)
        _key = pack_entry(sub_window, default_text="在此处输入密码")
        pack_button(sub_window, "确定", lambda: settings_key(get_entry(_key), sub_window), x=80, y=70)
        pack_button(sub_window, "清空", lambda: delete_entry(_key), x=0, y=70)

        sub_window.mainloop()

    # 切勿使用elif
    if temp['settings_if']:
        sub_window = tk.Tk()
        sub_window.title("app settings")
        sub_window.geometry(win_geometry)
        sub_window.resizable(win_resizable[0], win_resizable[1])

        pack_button(sub_window, "返回", lambda: [close_win(sub_window), deiconify_win(win)], x=160, y=70)
        pack_button(sub_window, '重置', lambda: r_configure(), y=70)

        pack_message(sub_window, '修改&重置后请重启应用')

        pack_message(sub_window, '模式:', y=20)
        _mode = pack_entry(sub_window, x=50, y=20)
        pack_button(
            sub_window,
            '保存',
            lambda: [save_settings(get_entry(_mode)), delete_entry_s([_mode])],
            x=80,
            y=70
        )

        sub_window.mainloop()

    deiconify_win(win)


if __name__ == "__main__":
    main()
