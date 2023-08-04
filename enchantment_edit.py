import tkinter as tk
from tkinter import ttk
import csv


def read_enchantment_list():
    """读取命令列表，并返回一个列表，里面有每个附魔的译名及其ID的元组"""
    enchantments = []
    with open("enchantment_list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            enchantments.append((row["Name"], row["ID"], row["Type"]))
    return enchantments


# 创建窗口，并初始化
window = tk.Tk()
window.title("附魔编辑器")  # 设置标题
window.resizable(False, False)  # 禁止调整窗口大小
window.iconbitmap("command_generator.ico")  # 设置图标

tab_name_list = ["剑/斧附魔", "弓附魔", "弩附魔", "三叉戟附魔", "盔甲附魔", "工具附魔", "通用附魔"]
tab_list = []
name_dict = {
    "剑/斧附魔": "sword",
    "弓附魔": "bow",
    "弩附魔": "crossbow",
    "三叉戟附魔": "trident",
    "盔甲附魔": "armor",
    "工具附魔": "tool",
    "通用附魔": "common",
}
for i, tab_name in enumerate(tab_name_list):
    tab_list.append(ttk.LabelFrame(text=tab_name))
    tab_list[-1].grid(column=0, row=i, padx=8, pady=4, sticky=tk.W)

enchantment_list = read_enchantment_list()
choose_list = []
check_button_list = []
level_list = []
level_entered_list = []

for i in range(len(enchantment_list)):
    choose_list.append(tk.BooleanVar())
    level_list.append(tk.IntVar(value=1))

for tab, tab_name in zip(tab_list, tab_name_list):
    counter = 0
    for i, enchantment in enumerate(enchantment_list):
        name, id, type = enchantment
        if name_dict[tab_name] == type:
            check_button_list.append(
                ttk.Checkbutton(tab, text=name, variable=choose_list[i])
            )
            check_button_list[-1].grid(
                column=0 + counter % 2 * 3, row=counter // 2, padx=8, pady=2, sticky=tk.W
            )
            
            level_entered_list.append(ttk.Entry(tab, width=10, textvariable=level_list[i]))
            level_entered_list[-1].grid(
                column=1 + counter % 2 * 3, row=counter // 2, padx=0, pady=2, sticky=tk.W
            )
            ttk.Label(tab, text="级  ").grid(column=2 + counter % 2 * 3, row=counter // 2)
            counter += 1

window.mainloop()
