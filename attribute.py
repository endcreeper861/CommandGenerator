from typing import Literal

from mc_uuid import UUID, generate_uuid
from nbt import NBT


class AttributeModifier:
    """Minecraft中物品属性修饰符的类"""

    def __init__(
        self,
        amount: float,
        attribute_name: str,
        name: str,
        operation: Literal[0, 1, 2],
        slot: Literal["mainhand", "offhand", "head", "chest", "legs", "feet"]
        | None = None,
        uuid: UUID | None = None,
    ) -> None:
        """
        amount:
            计算中修饰符调整基础值的数值。
        attribute_name:
            此修饰符的属性名称，是一个命名空间ID。
        name:
            修饰符的名称。
        Operation:
            属性修饰符的运算方法。
        Slot:
            指定修饰符产生效果的槽位。值只能为mainhand(主手)、offhand(副手)、
            head(头盔)、chest(胸甲)、legs(护腿)或feet(靴子)。如果此值不存在，则
            上述6个槽位上此属性修饰符都可以发挥作用。
        UUID:
            属性的UUID，以4个32位整数的形式存储。
        """
        self.amount = amount
        self.attribute_name = attribute_name
        self.name = name
        self.operation = operation
        self.slot = slot
        if uuid is None:
            self.uuid = generate_uuid(
                f"{amount}{attribute_name}{name}{operation}{slot}".encode()
            )

    def __str__(self) -> str:
        return str(
            NBT(
                Amount=self.amount,
                AttributeName=self.attribute_name,
                Name=self.name,
                Slot=self.slot,
                Operation=self.operation,
                UUID=self.uuid,
            )
        )


class Attribute:
    """Minecraft中实体属性的类"""