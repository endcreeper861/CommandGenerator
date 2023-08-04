from commands import Give
from item import Item
from nbt import NBT
from enchantment import Enchantment

block_list = [
    "minecraft:diamond_ore",
    "minecraft:stone",
]
my_item = Item("minecraft:diamond_pickaxe", damage=999, can_destroy=block_list)
command = Give("@s", my_item)
print(my_item)
print(command)

my_item = Item("minecraft:diamond_pickaxe")
command = Give("@s", my_item)
print(my_item)
print(command)

enchantment_list = [
    Enchantment("minecraft:fortune", 3),
    Enchantment("minecraft:efficiency", 5),
    Enchantment("minecraft:unbreaking", 3),
    Enchantment("minecraft:mending", 1),
]
my_item = Item("minecraft:diamond_pickaxe", enchantments=enchantment_list)
command = Give("@s", my_item)
print(my_item)
print(command)