from nbt import NBT


class Item:
    """Minecraft物品的标准类"""

    def __init__(
        self,
        id: str,
        count: int = 1,
        damage: int = 0,
        hide_flags: int = 0,
        unbreakable: bool = False,
        can_destroy: list = [],
        can_place_on: list = [],
        tags: list = [],
        **kwargs
    ) -> None:
        """
        id:
            物品/方块ID。若未指定，游戏会在加载区块或者生成物品时将其变更为空。
        count:
            堆叠在当前物品栏中的物品数量。任何物品都能被堆叠，包括工具、盔甲、运输工
            具。范围从-128到127。数值为1时不被游戏显示。小于1的数值显示为红色。
        damage:
            物品的损害值。默认为0。
        hide_flags:
            决定隐藏显示物品的哪些信息，以按位或二进制进行保存。1代表隐藏
            Enchantments的附魔信息，2代表隐藏AttributeModifiers的属性修饰符信息，4
            代表隐藏Unbreakable的无法破坏信息，8代表隐藏CanDestroy的可破坏方块信
            息，16代表隐藏CanPlace的可放置方块信息，32代表隐藏其他附加信息，64代表隐
            藏display.color的染色信息，128代表隐藏Trim的盔甲纹饰信息。当此值为255时，
            所有附加信息都不显示。
        unbreakable:
            表示物品是否无法破坏。
        can_destroy:
            冒险模式的玩家可以使用这个物品破坏的方块列表。
        can_place_on:
            冒险模式的玩家可以将方块放置在其表面的方块列表。
        tags:
            该物品的标签列表。
        除此以外，还可以自己指定想要的NBT标签。示例：
        `my_item = Item("minecraft:diamond_pickaxe", a=1, b="something", c=[3, 1, 4])`
        """
        self.count = count
        self.id = id
        nbt = {}
        if damage != 0 :
            nbt["Damage"] = damage
        if hide_flags != 0:
            nbt["HideFlags"] = hide_flags
        if unbreakable:
            nbt["Unbreakable"] = True
        if can_destroy != []:
            nbt["CanDestroy"] = can_destroy
        if can_place_on != []:
            nbt["CanPlaceOn"] = can_place_on
        if tags != []:
            nbt["Tags"] = tags
        nbt.update(kwargs)
        self.nbt = NBT(**nbt)

    def __str__(self) -> str:
        string = str(NBT(Count=self.count, id=self.id, tag=self.nbt.dict))
        return string

    def give(self):
        """获取用于give命令的物品形式的字符串"""
        text = f"{self.id}{self.nbt}"
        return text
