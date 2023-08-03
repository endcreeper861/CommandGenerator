import csv
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from pyperclip import copy

from commands import Give
from item import Item


def read_item_list():
    """读取物品列表并返回所有物品的ID"""
    item_list = []
    with open("item_list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            item_list.append(row["Name"])
    return item_list


def find_item(name: str):
    """读取物品列表，并根据中文名找到物品ID"""
    with open("item_list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["Name"] == name:
                return "minecraft:" + row["ID"]
    return "minecraft:air"


def generate():
    """生成一条命令"""
    hide_flags = (
        1 * hide_enchantment.get()
        + 2 * hide_attribute.get()
        + 4 * hide_unbreakable.get()
        + 8 * hide_can_destroy.get()
        + 16 * hide_can_place.get()
        + 32 * hide_other.get()
        + 64 * hide_color.get()
        + 128 * hide_trim.get()
    )
    if item.get() in read_item_list():
        item_name = find_item(item.get())
    else:
        item_name = item.get()
    custom_item = Item(
        item_name,
        count.get(),
        damage.get(),
        hide_flags,
        unbreakable.get(),
        can_destroy_text.get(1.0, "end").split(),
        can_place_text.get(1.0, "end").split(),
        tags_text.get(1.0, "end").split(),
    )
    command = Give("@s", custom_item)
    return str(command)


def generate_and_show():
    """生成一条命令并将其放到展示区"""
    command = generate()
    command_text.config(state=tk.NORMAL)
    command_text.delete(1.0, "end")
    command_text.insert("end", command)
    command_text.config(state=tk.DISABLED)

def generate_and_copy():
    """生成一条命令并将其放到展示区，再复制到剪贴板"""
    command = generate()
    command_text.config(state=tk.NORMAL)
    command_text.delete(1.0, "end")
    command_text.insert("end", command)
    command_text.config(state=tk.DISABLED)
    copy(command)


# 创建窗口，并初始化
window = tk.Tk()
window.title("命令生成器")  # 设置标题
window.geometry("430x700")  # 设置大小
window.resizable(False, False)  # 禁止调整窗口大小
window.iconbitmap("command_generator.ico")  # 设置图标

# 创建命令选择器
ttk.Label(text="选择命令：").grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)
command = tk.StringVar()
command_chosen = ttk.Combobox(width=12, textvariable=command)
command_chosen["values"] = ("give",)
command_chosen.grid(column=0, row=0, padx=80, pady=4, sticky=tk.W)
command_chosen.current(0)  # 设置初始显示值，值为元组['values']的下标
command_chosen.config(state="readonly")  # 设为只读模式

# 创建give命令的窗口
# 基础设定
basic_setting = ttk.LabelFrame(text="基础设定")
basic_setting.grid(column=0, row=1, padx=8, pady=4, sticky=tk.W)

ttk.Label(basic_setting, text="选择/输入物品id：").grid(column=0, row=0)  # 输入物品名称
item = tk.StringVar()
item_chosen = ttk.Combobox(basic_setting, width=39, textvariable=item)
item_chosen.focus()
item_chosen["values"] = read_item_list()
item_chosen.grid(column=1, row=0)
item_chosen.current(0)

ttk.Label(basic_setting, text="物品数量：").grid(column=0, row=1)  # 输入数量
count = tk.IntVar(value=1)
count_entered = ttk.Entry(basic_setting, width=12, textvariable=count)
count_entered.grid(column=1, row=1)

ttk.Label(basic_setting, text="损害值：").grid(column=0, row=2)  # 输入损害值
damage = tk.IntVar()
damage_entered = ttk.Entry(basic_setting, width=12, textvariable=damage)
damage_entered.grid(column=1, row=2)

# 标签列表
ttk.Label(basic_setting, text="标签(每行一个)：").grid(column=0, row=3)
tags_text = ScrolledText(basic_setting, width=39, height=3, wrap="none")
tags_text.grid(column=1, row=3)

# 一次性控制各控件之间的距离
for child in basic_setting.winfo_children():
    child.grid_configure(padx=3, pady=1, sticky=tk.N + tk.W)

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

# 可破坏方块列表
ttk.Label(advanced_setting, text="可破坏方块列表(每行一个)：").grid(column=0, row=2)
can_destroy_text = ScrolledText(advanced_setting, width=55, height=5, wrap="none")
can_destroy_text.grid(column=0, row=3)

# 可放置方块列表
ttk.Label(advanced_setting, text="可放置方块列表(每行一个)：").grid(column=0, row=4)
can_place_text = ScrolledText(advanced_setting, width=55, height=5, wrap="none")
can_place_text.grid(column=0, row=5)

# 一次性控制各控件之间的距离
for child in advanced_setting.winfo_children():
    child.grid_configure(padx=3, pady=1, sticky=tk.W)


# 命令生成区
generate_area = ttk.LabelFrame(text="命令生成区")
generate_area.grid(column=0, row=4, padx=8, pady=4, sticky=tk.W)

# 生成命令按钮
generate_button = ttk.Button(
    generate_area, text="生成命令", width=20, command=generate_and_show
)
generate_button.grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)
copy_button = ttk.Button(
    generate_area, text="生成命令并复制到剪贴板", width=20, command=generate_and_copy
)
copy_button.grid(column=0, row=0, padx=8, pady=4, sticky=tk.E)
command_text = ScrolledText(generate_area, width=55, height=5, wrap="char")
command_text.grid(column=0, row=1, padx=3, pady=1, sticky=tk.W)
command_text.config(state=tk.DISABLED)

window.mainloop()  # 启动GUI
