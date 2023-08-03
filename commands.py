from item import Item
from selector import Selector


class Give:
    """给予实体一种指定数量的物品。"""

    def __init__(self, target: str | Selector, item: Item) -> None:
        """
        target:
            必须为玩家名、目标选择器或UUID。
        item:
            指定给予的物品。必须为Item类。
        """
        self.target = target
        self.item = item

    def __str__(self) -> str:
        command = f"/give {self.target} {self.item.give()} {self.item.count}"
        return command
    

class Setblock:
    """将指定位置的方块更改为另一个方块。"""
    def __init__(self, pos, block, ) -> None:
        pass