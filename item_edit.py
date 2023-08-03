import csv
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def read_item_list():
    """读取物品列表并返回所有物品的ID"""
    item_list = []
    with open("item_list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            item_list.append(row["Name"])
    return item_list


def find_item(name:str):
    """读取物品列表，并根据中文名找到物品ID"""


# 创建窗口，并初始化
window = tk.Tk()
window.title("物品/方块编辑器")  # 设置标题
window.geometry("430x700")  # 设置大小
window.resizable(False, False)  # 禁止调整窗口大小
window.iconbitmap("command_generator.ico")  # 设置图标

# 创建物品编辑器的窗口
# 基础设定
basic_setting = ttk.LabelFrame(text="基础设定")
basic_setting.grid(column=0, row=1, padx=8, pady=4, sticky=tk.W)

ttk.Label(basic_setting, text="选择/输入物品id：").grid(column=0, row=0)  # 输入物品名称
item = tk.StringVar()
item_chosen = ttk.Combobox(basic_setting, width=39, textvariable=item)
item_chosen["values"] = read_item_list()
item_chosen.grid(column=1, row=0)
item_chosen.current(0)

ttk.Label(basic_setting, text="物品数量：").grid(column=0, row=1)  # 输入数量
count = tk.IntVar()
count_entered = ttk.Entry(basic_setting, width=12, textvariable=count, show="1")
count_entered.grid(column=1, row=1)

ttk.Label(basic_setting, text="损害值：").grid(column=0, row=2)  # 输入损害值
damage = tk.IntVar()
damage_entered = ttk.Entry(basic_setting, width=12, textvariable=damage)
damage_entered.grid(column=1, row=2)

#标签列表
ttk.Label(basic_setting, text="标签(每行一个)：").grid(column=0, row=3)
tags = tk.StringVar()
tags_text = ScrolledText(basic_setting, width=39, height=3, wrap="none")
tags_text.grid(column=1, row=3)

# 一次性控制各控件之间的距离
for child in basic_setting.winfo_children():
    child.grid_configure(padx=3, pady=1, sticky=tk.N+tk.W)

# 进阶设定
advanced_setting = ttk.LabelFrame(text="进阶设定")
advanced_setting.grid(column=0, row=2, padx=8, pady=4, sticky=tk.W)

unbreakable = tk.BooleanVar()  # 无法破坏标签
unbreakable_check = ttk.Checkbutton(advanced_setting, text="无限耐久", variable=unbreakable)
unbreakable_check.grid(column=0, row=0)

# 以下这一坨全是隐藏信息
hide_infos = ttk.LabelFrame(advanced_setting, text="鼠标停留在物品时隐藏的信息")
hide_infos.grid(column=0, row=1, padx=8, pady=4, sticky=tk.W)
hide_enchantment = tk.BooleanVar()
hide_enchantment_check = ttk.Checkbutton(
    hide_infos, text="附魔信息", variable=hide_enchantment
)
hide_enchantment_check.grid(column=0, row=0)
hide_attribute = tk.BooleanVar()
hide_attribute_check = ttk.Checkbutton(hide_infos, text="属性信息", variable=hide_attribute)
hide_attribute_check.grid(column=1, row=0)
hide_unbreakable = tk.BooleanVar()
hide_unbreakable_check = ttk.Checkbutton(
    hide_infos, text="无法破坏", variable=hide_unbreakable
)
hide_unbreakable_check.grid(column=2, row=0)
hide_can_destroy = tk.BooleanVar()
hide_can_destroy_check = ttk.Checkbutton(
    hide_infos, text="可破坏方块", variable=hide_can_destroy
)
hide_can_destroy_check.grid(column=3, row=0)
hide_can_place = tk.BooleanVar()
hide_can_place_check = ttk.Checkbutton(
    hide_infos, text="可放置方块", variable=hide_can_place
)
hide_can_place_check.grid(column=4, row=0)
hide_other = tk.BooleanVar()
hide_other_check = ttk.Checkbutton(hide_infos, text="其他信息", variable=hide_other)
hide_other_check.grid(column=0, row=1)
hide_color = tk.BooleanVar()
hide_color_check = ttk.Checkbutton(hide_infos, text="染色信息", variable=hide_color)
hide_color_check.grid(column=1, row=1)
hide_trim = tk.BooleanVar()
hide_trim_check = ttk.Checkbutton(hide_infos, text="盔甲纹样", variable=hide_trim)
hide_trim_check.grid(column=2, row=1)
for child in hide_infos.winfo_children():
    child.grid_configure(padx=1, sticky=tk.W)

#可破坏方块列表
ttk.Label(advanced_setting, text="可破坏方块列表(每行一个)：").grid(column=0, row=2)
can_destroy = tk.StringVar()
can_destroy_text = ScrolledText(advanced_setting, width=55, height=5, wrap="none")
can_destroy_text.grid(column=0, row=3)

#可放置方块列表
ttk.Label(advanced_setting, text="可放置的方块列表(每行一个)：").grid(column=0, row=4)
can_destroy = tk.StringVar()
can_destroy_text = ScrolledText(advanced_setting, width=55, height=5, wrap="none")
can_destroy_text.grid(column=0, row=5)

# 一次性控制各控件之间的距离
for child in advanced_setting.winfo_children():
    child.grid_configure(padx=3, pady=1, sticky=tk.W)


window.mainloop()  # 启动GUI