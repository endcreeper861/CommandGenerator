from nbt import NBT


class Enchantment:
    """Minecraft附魔的类"""

    def __init__(self, id: str, level: int) -> None:
        """
        id:
            魔咒的命名空间ID。
        level:
            魔咒的等级，1表示等级1。读取时会将数值限定到0至255之间（含边界）。
        """
        self.id = id
        self.level = level
    
    def __str__(self) -> str:
        return str(NBT(id=self.id, lvl=self.level))
