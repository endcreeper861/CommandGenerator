import tkinter as tk
from csv import DictReader
from itertools import compress
from tkinter import ttk

from enchantment import Enchantment


def ask_enchantments(
    chosen_enchantments: list[Enchantment] | None = None,
) -> list[Enchantment]:
    """创建窗口以获取物品的附魔信息"""
    if chosen_enchantments is None:
        chosen_enchantments = []

    def read_enchantment_list():
        """读取命令列表，并返回一个列表，里面有每个附魔的译名及其ID的元组"""
        enchantments = []
        with open("enchantment_list.csv", encoding="utf-8") as f:
            for row in DictReader(f):
                enchantments.append((row["Name"], row["ID"], row["Type"]))
        return enchantments

    def destroy_quit():
        """保存所选的命令并退出"""
        window.destroy()
        window.quit()

    # 创建窗口，并初始化
    window = tk.Tk()
    window.title("附魔编辑器")  # 设置标题
    window.resizable(False, False)  # 禁止调整窗口大小
    window.iconbitmap("command_generator.ico")  # 设置图标

    area_name_list = ["剑/斧附魔", "弓附魔", "弩附魔", "三叉戟附魔", "盔甲附魔", "工具附魔", "通用附魔"]
    name_dict = {
        "剑/斧附魔": "sword",
        "弓附魔": "bow",
        "弩附魔": "crossbow",
        "三叉戟附魔": "trident",
        "盔甲附魔": "armor",
        "工具附魔": "tool",
        "通用附魔": "common",
    }
    area_list = []
    for i, area_name in enumerate(area_name_list):
        area_list.append(ttk.LabelFrame(window, text=area_name))
        area_list[-1].grid(column=0, row=i, padx=8, pady=4, sticky=tk.W)

    all_enchantment_list = read_enchantment_list()
    choose_list = []
    level_list = []
    # 这一步很重要，是将一个包含了很多Enchantment类的列表转换为一个字典
    # 并且以id作为键，level作为值
    chosen_enchantments = dict((enchantment.id, enchantment.level) for enchantment in chosen_enchantments)  # type: ignore

    for i, enchantment in enumerate(all_enchantment_list):
        id = enchantment[1]
        if id in chosen_enchantments.keys():  # type: ignore
            choose_list.append(tk.BooleanVar(window, value=True))
            level_list.append(tk.IntVar(window, value=chosen_enchantments[id]))  # type: ignore
        else:
            choose_list.append(tk.BooleanVar(window, value=False))
            level_list.append(tk.IntVar(window, value=1))

    for area, area_name in zip(area_list, area_name_list):
        counter = 0
        for i, enchantment in enumerate(all_enchantment_list):
            name, id, type = enchantment
            if name_dict[area_name] == type:
                ttk.Checkbutton(
                    area, text=name.ljust(5, "\u3000"), variable=choose_list[i]
                ).grid(
                    column=0 + counter % 2 * 3,
                    row=counter // 2,
                    padx=8,
                    pady=1,
                    sticky=tk.W,
                )

                ttk.Entry(area, width=10, textvariable=level_list[i]).grid(
                    column=1 + counter % 2 * 3,
                    row=counter // 2,
                    padx=0,
                    pady=1,
                    sticky=tk.W,
                )
                ttk.Label(area, text="级  ").grid(
                    column=2 + counter % 2 * 3, row=counter // 2
                )
                counter += 1

    ttk.Button(window, text="完成", width=55, command=destroy_quit).grid(
        column=0, row=len(area_name_list) + 1, padx=8, pady=4
    )
    window.mainloop()

    # 检测已经选择的附魔
    enchantment_list = list(
        compress(
            (
                Enchantment(all_enchantment_list[i][1], level_list[i].get())
                for i in range(len(choose_list))
            ),
            (choose.get() for choose in choose_list),
        )
    )
    return enchantment_list


if __name__ == "__main__":
    enchantments = ask_enchantments([Enchantment("minecraft:mending", 1)])
    print(enchantments)
